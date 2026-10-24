# Export a reviewable identity kit

Use this procedure when delivering editable brand assets, print candidates or a
website preview. Keep the approved brief, original sources, license evidence,
exact candidate revision and performed checks together. A local review package
does not establish adoption, production approval or public availability.

## Source and output ownership

Make the source checkout an explicit argument to export scripts. A script copied
into a delivery folder cannot assume that a fixed number of parent directories
still reaches the original repository. Either ship the required source layout
and licensed inputs, or document the source checkout and an explicit
`--source-root`/equivalent command. Test the copied command from another working
directory. Editable vector files can remain independently useful when rebuild
dependencies are unavailable; describe that limitation.

Require a new output root, including rejecting empty existing folders and
broken symlink entries. Create it exclusively at export time; a preflight check
alone is not a filesystem lock. Do not merge a fresh export into an older kit:
removed pages, private notes and stale assets can otherwise survive. Stage a
replacement separately and verify it before the owner retires an earlier copy.

The optional [export checker](../scripts/check_export.py) offers a read-only
path preflight and exact website inventory/hash comparison using Python's
standard library. It does not create an output, copy files, decode QR codes,
classify rights or publish. Its manifest format is compatible with the release
plugin's static manifest (`version: 1`, `files: {relative_path: sha256}`). Supply
a separately reviewed list of intended public files; generating an allowlist
from the output being checked would bless its accidental contents.

```sh
python3 check_export.py preflight --source-root /absolute/source --output-root /new/absolute/kit
python3 check_export.py payload --payload-root /absolute/kit/website-preview --manifest /absolute/reviewed-public-files.json
```

## Separate the kit from its website payload

A kit may include editable sources, license records, review notes, production
guides and print files. Its website payload should contain only the consumer's
explicit public allowlist. Keep the preview instructions, hashes and reports
outside that payload. Verify both the exact path set and every file hash; a
matching count cannot detect one unexpected file replacing a required asset.
Reject linked files/directories and unsafe manifest paths. Inspect the selected
allowlist itself for private content; hashes establish identity, not permission
or safety of the content.

Record source and rendered artifact hashes separately when a build transforms
files. Test the actual exported preview with its intended local server, direct
entry URL, relative assets, navigation and support path. Rebuild affected
exports after source changes and invalidate the corresponding prior checks.

## QR and print evidence

Record the intended literal destination. Decode the QR from the final exported
PDF raster at a stated resolution and crop, not only from the source matrix or
standalone SVG. Confirm its quiet zone, contrast, printed dimensions and absence
of overlays. A source QR can be correct while the final export clips or scales it
into an unusable result. Record the final PDF/raster hash, decoder and observed
URL. If decoding is unavailable, leave this check unperformed.

A successful software decode does not establish camera performance on physical
stock. Preserve separate checks for actual printing, glare/lighting, camera and
distance, printer color profile, bleed/cut, fabric/ink and vendor proofs. Keep
editable production candidates distinct from certified printer-specific files,
embroidery files or completed manufacturing approval. Verify public destination
content and the next action before distributing printed materials; an HTTP
success alone cannot establish the intended journey or product availability.

## Handoff

State what is ready, the exact inputs and exports inspected, and the remaining
owner, physical, vendor and deployment decisions. Report design preferences as
judgment and observed failures as defects. Do not turn a polished mockup, QR scan,
preview visit or unit test into a customer, conversion or accessibility claim.
