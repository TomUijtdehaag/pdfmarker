from pdfmarker import Colors, Highlight, Marker

marker = Marker.from_disk(path="tests/data/test.pdf")

marker.add(
    [Highlight("Sample", group="test"), Highlight("con", group="test", color=Colors.red, subwords=True)]
)

marker.add(Highlight("simple", group="max"))

marker.to_disk("example_marked.pdf")
