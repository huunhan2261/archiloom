# videos/

Drop demo `.mp4` files here for tools whose `TOOLS` entry uses `type: "file"`
in `docs/index.html`.

Naming: match the path you set in the tool's `video` field, e.g.

```js
{
  name: "Batch Family Rename",
  video: "videos/batch-family-rename.mp4",
  type: "file",
  ...
}
```

Suggested convention: kebab-case the tool name (`Batch Family Rename` →
`batch-family-rename.mp4`) so the file is easy to match back to its entry
in `TOOLS`.

Tools that use `type: "youtube"` don't need a file here — their `video`
field is a YouTube embed URL instead.

Recording size: the existing captures are 1400x850 (Family and Detailing),
1500x950 (Checking), and 1920x1040 (camwalk).
Any aspect ratio works — the modal reads each file's real dimensions on
`loadedmetadata` and sizes its frame to match — but keeping new recordings at
one size per batch keeps the demos consistent. Keep files well under GitHub's 100 MB limit;
they are committed straight to the repo and served by GitHub Pages.
