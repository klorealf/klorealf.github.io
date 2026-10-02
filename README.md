# khadijafranklin.me: your website guide

Your site is hosted free on **GitHub Pages**, using the domain you bought
from **Hostinger**. GitHub holds the files; Hostinger points your domain at them.

## What's in this folder

| File | What it does | Upload to GitHub? |
|---|---|---|
| index.html | All the page content (text, sections, links) | Yes |
| css/style.css | Colors, fonts, spacing, layout | Yes |
| js/script.js | Mobile menu, active link, copy-email button, code viewer | Yes |
| python/batch_scaler.py | The Live Demo tool, written in Python | Yes |
| images/ | Your KLF logo and browser-tab icon | Yes |
| resume.pdf | Your resume (you add this) | Yes |
| CNAME | Tells GitHub your domain name (one line: khadijafranklin.me) | Yes |
| serve.py | Preview the site on your computer | Optional |
| make_qr.py, qr-code.png | Your networking QR code | Optional |
| README.md | This guide | Optional |

**How the Python works:** GitHub Pages only serves files; it can't run Python
on its servers. PyScript gets around that by running batch_scaler.py inside the
visitor's own browser, so it works anywhere.

---

## Part 1: Get your files ready

1. **Your email** (khadija@khadijafranklin.me) is already in index.html.
   To change it later, search for it and replace it in both places.
2. **Add your resume.** Save it as a PDF, name it exactly `resume.pdf`
   (lowercase), and put it in this folder next to index.html.
3. **Preview it.** Open a terminal in this folder and run `python serve.py`
   (or `python3 serve.py` on a Mac). Your browser opens the site.
   Press Ctrl+C in the terminal to stop.
   Use serve.py rather than double-clicking index.html; the code viewer
   needs a server to load the Python file.

---

## Part 2: Put your projects on GitHub and link them

### A. Polish your GitHub profile (you already have an account)
Click your profile picture, then **Your profile**, then **Edit profile**.
Add your name, a one-line bio, and `https://khadijafranklin.me` as your website.

### B. Create a repository for a project
A repository ("repo") is one folder for one project.
1. Click the **+** at the top right, then **New repository**.
2. **Repository name:** short, with dashes, e.g. `chemical-interaction-checker`.
3. **Description:** one sentence about what it does.
4. Set it to **Public** so employers can see it.
5. Tick **Add a README file**.
6. Click **Create repository**.

### C. Upload your code
1. In your new repo, click **Add file**, then **Upload files**.
2. Drag your project files into the box.
3. Under **Commit changes**, type a short note like `First upload`.
4. Click **Commit changes**.

### D. Copy the link
Your repo's link is the address in the browser bar, in this format:
`https://github.com/klorealf/REPO-NAME`

### E. Add the link to your website
1. Open index.html and find the project (search for its name, e.g.
   `Chemical Interaction Checker`).
2. Just below it, find this line:
   ```html
   <a href="#" class="project-link">View on GitHub</a>
   ```
3. Replace the `#` with your link, and add `target="_blank" rel="noopener"`
   so it opens in a new tab:
   ```html
   <a href="https://github.com/klorealf/chemical-interaction-checker" class="project-link" target="_blank" rel="noopener">View on GitHub</a>
   ```
4. Save, preview with serve.py, and click the link to test it.
5. Upload the updated index.html to your website repo
   (see "Making changes later" in Part 3).

**Tip:** Do the same for the Dupe Checker. For the ITIAH Angels card, use
their website address instead of a GitHub link.

---

## Part 3: Put the site live (GitHub Pages + your Hostinger domain)

Your GitHub username is `klorealf`, so your website repo is `klorealf.github.io`.

### Step 1: Create the website repository
1. On GitHub, click the **+** at the top right, then **New repository**.
2. **Repository name:** `klorealf.github.io` (exactly that, with your
   username). This special name tells GitHub it's a website.
3. Set it to **Public**. Don't tick "Add a README" (you already have one).
4. Click **Create repository**.

### Step 2: Upload your website files
1. On the new repo's page, click **uploading an existing file**
   (or **Add file**, then **Upload files**).
2. Open your website folder on your computer and drag in **everything inside
   it**: index.html, CNAME, resume.pdf, and the css, js, python and images
   folders. Drag the folders themselves so their names are kept.
   (Drag the contents, not the outer folder, so index.html sits at the top level.)
3. Type a note like `Launch website` and click **Commit changes**.
4. Check the repo's main page: you should see index.html and CNAME listed
   directly, with the folders beside them.

### Step 3: Turn on GitHub Pages
1. In the repo, click **Settings** (top menu), then **Pages** (left menu).
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to **main** and the folder to **/ (root)**. Click **Save**.
4. After a minute or two, your site works at `https://klorealf.github.io`.
   Open it to check before connecting the domain.

### Step 4: Point your Hostinger domain at GitHub
1. Log in to **hPanel** and go to **Domains**, then click
   **khadijafranklin.me**.
2. Open **DNS / Nameservers**, then **DNS records**.
3. **Delete** any existing record with Type **A** and Name **@**, and any
   record with Type **CNAME** and Name **www**. (These point to Hostinger's
   parking page.)
   **Don't touch any MX, TXT, or CNAME records with "mail", "autodiscover",
   "_dmarc" or "hostingermail" in them. Those run your email
   (khadija@khadijafranklin.me), and deleting them stops it working.**
4. **Add four A records**, one at a time. For each: Type **A**, Name **@**,
   TTL left as is, and these values:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
5. **Add one CNAME record:** Type **CNAME**, Name **www**,
   Target `klorealf.github.io`
6. Save. Changes usually work within an hour but can take up to 24 hours.

### Step 5: Connect the domain on GitHub and turn on https
1. Back in GitHub: **Settings**, then **Pages**.
2. Under **Custom domain**, you should see `khadijafranklin.me`
   (from your CNAME file). If not, type it in and click **Save**.
3. Wait for the green **DNS check successful** message. Refresh the page now
   and then; it can take a while.
4. Tick **Enforce HTTPS**. If it's greyed out, GitHub is still creating your
   security certificate; check back in an hour. Your QR code uses https, so
   this step matters.

### Step 6: Test it
1. Visit `https://khadijafranklin.me` on your computer and your phone.
   Also try `www.khadijafranklin.me`; it should land on the same site.
2. Check: the menu works on your phone, the Resume link opens, the Live Demo
   button changes from "Loading Python..." to "Scale my batch" and works.
3. Scan your QR code with your phone camera.
4. Seeing an old version? Refresh with **Ctrl+Shift+R** (Windows) or
   **Cmd+Shift+R** (Mac).

### Making changes later
1. Edit the file on your computer and preview it with serve.py.
2. In your `klorealf.github.io` repo, click **Add file**, then
   **Upload files**, and drag in the changed file (into the same folder it
   lives in). GitHub replaces the old version.
3. Click **Commit changes**. The live site updates within a minute or two.

---

## Part 4: Networking

- Save qr-code.png to your phone's photos so people can scan it from your
  screen. Printed, keep it at least 1 inch (2.5 cm) wide.
- Add `https://khadijafranklin.me` to LinkedIn: **Edit profile**, then
  **Contact info**, then **Website**.
