# Sources

- EBU, Recommendation R 128, "Loudness normalisation and permitted maximum level of audio signals," https://tech.ebu.ch/docs/r/r128.pdf (verified 2026-11-26). Programme loudness −23.0 LUFS; true peak not above −1 dBTP during production. Use this as a cited broadcast reference, not as a silent default for game or UI cues.
- ITU, Recommendation ITU-R BS.1770, "Algorithms to measure audio programme loudness and true-peak audio level," https://www.itu.int/rec/R-REC-BS.1770 (verified 2026-11-26). Measurement method behind LUFS/LKFS and true peak.
- FFmpeg, `ebur128` filter, https://ffmpeg.org/ffmpeg-filters.html#ebur128 (verified 2026-11-26). Common local implementation of the EBU/ITU loudness measurement.
- fal.ai, "fal-ai/audio-understanding," https://fal.ai/models/fal-ai/audio-understanding (verified 2026-11-26). Public example of an audio-understanding endpoint for a second opinion. This skill does not require that vendor.

Do not copy vendor account identifiers or API keys into this repository.
