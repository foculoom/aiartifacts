// Compile through compile_launcher.py with a reviewed private profile.
// Secret bytes travel only to the pinned runner through a pipe; no getter exists.
import Foundation
import Security
import CryptoKit

func stop(_ code: Int32) -> Never { exit(code) }
guard CommandLine.arguments.count >= 2 else { stop(64) }
let operation = CommandLine.arguments[1]
// LaunchConfig is generated from the reviewed private profile at local compile
// time. There is no operation that exports the Keychain value to the caller.
let service = LaunchConfig.service
let account = LaunchConfig.account
var query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: service,
    kSecAttrAccount as String: account
]
if operation == "store" {
    guard CommandLine.arguments.count == 2 else { stop(64) }
    let data = FileHandle.standardInput.readDataToEndOfFile()
    guard data.count >= 20 && data.count < 32768,
          let token = String(data: data, encoding: .utf8),
          !token.contains(where: { $0.isWhitespace }) else { stop(65) }
    // Default macOS ACL trusts the creating executable, not every application.
    // Existing items are never silently replaced or their ACL broadened.
    query[kSecValueData as String] = data
    query[kSecAttrSynchronizable as String] = false
    let status = SecItemAdd(query as CFDictionary, nil)
    stop(status == errSecSuccess ? 0 : (status == errSecDuplicateItem ? 73 : 74))
} else if operation == "run" {
    guard CommandLine.arguments.count == 3,
          LaunchConfig.tasks.contains(CommandLine.arguments[2]) else { stop(64) }
    for (path, expected) in LaunchConfig.files {
        guard let data = FileManager.default.contents(atPath: path),
              SHA256.hash(data: data).map({ String(format: "%02x", $0) }).joined() == expected else { stop(78) }
    }
    query[kSecReturnData as String] = true
    query[kSecMatchLimit as String] = kSecMatchLimitOne
    query[kSecUseAuthenticationUI as String] = kSecUseAuthenticationUIFail
    var value: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary, &value)
    guard status == errSecSuccess, let data = value as? Data else { stop(77) }
    let child = Process()
    let pipe = Pipe()
    child.executableURL = URL(fileURLWithPath: LaunchConfig.python)
    child.arguments = ["-I", LaunchConfig.runner, "--profile", LaunchConfig.profile,
                       "--task", CommandLine.arguments[2], "--service-input"]
    child.environment = ["HOME": NSHomeDirectory(), "PATH": "/usr/bin:/bin", "LANG": "en_US.UTF-8"]
    child.standardInput = pipe
    do {
        try child.run()
        pipe.fileHandleForWriting.write(data)
        try pipe.fileHandleForWriting.close()
        child.waitUntilExit()
        stop(child.terminationStatus)
    } catch { stop(74) }
} else { stop(64) }
