from fasthtml.common import Link, P, Style, Titled, fast_app, serve

app, rt = fast_app(
    pico=False,
    hdrs=(
        Link(rel="stylesheet", href="assets/normalize.min.css", type="text/css"),
        Link(rel="stylesheet", href="assets/sakura.css", type="text/css"),
        Style("p {color: red;}"),
    ),
)


@rt("/")
def get():
    return Titled(P("Hello World!"), hx_get="/change")


@rt("/change")
def get2():
    return P("Nice to be here!")


serve()
