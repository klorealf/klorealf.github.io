# =========================================================
# batch_scaler.py — Python that runs right in the visitor's browser
# PyScript (loaded in index.html) runs this file, so no server is needed
# and it works on regular Hostinger hosting.
#
# What it does: takes a formula written as percentages and works out
# how many grams of each ingredient you need for any batch size.
# =========================================================

# "pyscript" is the bridge between Python and the web page:
#   document = the page itself (like JavaScript's document)
#   when     = runs a Python function when something happens (a click)
from pyscript import document, when


def parse_formula(text):
    """Turn lines like 'Water, 70' into a list of (name, percent) pairs."""
    rows = []      # good lines go here
    problems = []  # lines we couldn't read go here
    # split("\n") breaks the text box into one line per ingredient
    # enumerate(..., 1) also counts the lines, starting at 1
    for line_number, line in enumerate(text.split("\n"), 1):
        line = line.strip()          # remove extra spaces at each end
        if not line:                 # skip blank lines
            continue
        # rsplit(",", 1) splits on the LAST comma only, so names with
        # commas (like "Water, Aqua") still work
        parts = line.rsplit(",", 1)
        if len(parts) != 2:
            problems.append(f"Line {line_number}: add a comma before the %")
            continue
        name = parts[0].strip()
        try:
            # remove a % sign if someone typed one, then convert to a number
            percent = float(parts[1].replace("%", "").strip())
        except ValueError:
            problems.append(f"Line {line_number}: '{parts[1].strip()}' isn't a number")
            continue
        rows.append((name, percent))
    return rows, problems


def scale(rows, batch_grams):
    """Work out grams for each ingredient: grams = percent / 100 x batch size."""
    return [(name, pct, pct / 100 * batch_grams) for name, pct in rows]


def safe(text):
    """Make text safe to put on the page (stops stray < or > breaking the HTML)."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_table(scaled, batch_grams):
    """Build the results table as HTML text."""
    total_pct = sum(pct for _, pct, _ in scaled)
    total_grams = sum(grams for _, _, grams in scaled)
    html = "<table><thead><tr><th>Ingredient</th><th>%</th><th>Grams</th></tr></thead><tbody>"
    for name, pct, grams in scaled:
        # :.2f means "show 2 decimal places"
        html += f"<tr><td>{safe(name)}</td><td>{pct:.2f}</td><td>{grams:.2f}</td></tr>"
    html += f"</tbody><tfoot><tr><td>Total</td><td>{total_pct:.2f}</td><td>{total_grams:.2f}</td></tr></tfoot></table>"
    # A real formula should add up to 100%, so warn if it doesn't
    if abs(total_pct - 100) > 0.01:
        html += f"<p class='demo-warn'>Heads up: this formula totals {total_pct:.2f}%, not 100%.</p>"
    return html


# @when("click", "#scale-btn") means: run this function when the
# button with id="scale-btn" is clicked
@when("click", "#scale-btn")
def on_scale(event):
    output = document.querySelector("#scale-output")
    text = document.querySelector("#formula-input").value
    try:
        batch = float(document.querySelector("#batch-size").value)
    except ValueError:
        output.innerHTML = "<p class='demo-warn'>Enter a batch size in grams.</p>"
        return
    if batch <= 0:
        output.innerHTML = "<p class='demo-warn'>Batch size must be more than 0.</p>"
        return

    rows, problems = parse_formula(text)
    if problems:
        # Show every line that needs fixing, one per line
        output.innerHTML = "<p class='demo-warn'>" + "<br>".join(safe(p) for p in problems) + "</p>"
        return
    if not rows:
        output.innerHTML = "<p class='demo-warn'>Add at least one ingredient.</p>"
        return

    output.innerHTML = build_table(scale(rows, batch), batch)


# This line runs once Python has finished loading: it switches the
# button on so visitors know the tool is ready
button = document.querySelector("#scale-btn")
button.disabled = False
button.innerText = "Scale my batch"
