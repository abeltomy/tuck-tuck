# Tuck Tuck

A typewriter for your browser. It looks and behaves like a manual machine: the
keys clack, the typebars fly up, the carriage moves, the bell rings near the end
of the line, and the page rolls up as you write. When you are done, take the
page with you as a `.txt` or `.md` file.

No install, no account, no tracking. One HTML file.

**Try it:** <https://abeltomy.github.io/tuck-tuck/>

## What it does

- **Types like a typewriter.** The typing point stays in the middle and the
  carriage moves under it. Each letter lands with its own slight tilt and ink
  weight.
- **Sounds like one.** Key strikes, space bar, back space, carriage return and
  the margin bell are synthesised with the Web Audio API, so there are no audio
  files to load. Switch **Key sounds** off to mute, or set the volume.
- **Returns the carriage for you.** The bell rings at column 48. The next space
  after it starts a new line, so you can keep typing. Press Return for a new
  paragraph.
- **Downloads your page.** `.txt` saves the text as typed. `.md` saves the same
  text as Markdown and keeps your line breaks. **Copy text** puts it on the
  clipboard.
- **Remembers your page.** The text is kept in your browser's local storage, so
  a refresh does not lose it. Nothing is sent anywhere.
- **Works on phones.** Tap the keys on the machine, or tap the paper to use your
  own keyboard. Drag the paper to read back.

## Keys

| Key | What happens |
| --- | --- |
| Any character | Typed at the typing point |
| Return | Carriage return and a new line |
| Back space | Erases the last character |
| Shift on the machine | Applies to the next key you tap |
| Mouse wheel or drag on the paper | Rolls the page so you can read back |
| Esc | Brings the page back to the typing point |

## Run it

Open `index.html` in a browser. If your browser blocks the fonts when the file
is opened straight from disk, serve the folder instead:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Put it on the web with GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, pick `main`
   and `/ (root)`, and save.

A minute later it is live at `https://<your-user>.github.io/<your-repo>/`.

## How it is built

Everything is in `index.html`: markup, styles and script. There is no build
step and no dependency.

- **Layout.** `layout()` breaks the text into lines the way the machine would:
  at every Return, at the first space after the bell, and when a word reaches
  the last column. The page is redrawn only where it changed.
- **Machine.** The body and keys are CSS. The typebar basket, ribbon, spools
  and bell are one inline SVG, animated from script.
- **Sound.** Each sound is a few bursts of filtered noise plus a short falling
  tone, with a little random variation so no two strikes are the same.
- **Settings.** `BELL`, `HARD` and `MARGIN` at the top of the script set the
  line length. The colours are CSS variables at the top of the stylesheet.

## Licence

Code: [MIT](LICENSE).

Fonts in `fonts/`: [Cutive Mono](https://github.com/googlefonts/cutivemono) and
[Jost](https://github.com/indestructible-type/Jost), both under the SIL Open
Font License 1.1. The licence texts are in the same folder.
