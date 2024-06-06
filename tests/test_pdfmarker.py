from hashlib import md5

from pdfmarker import Colors, Highlight, Marker


class TestHighlight:
    def test_init(self):
        highlight = Highlight("test")
        assert highlight.text == "test"
        assert highlight.group is None

    def test_eq(self):
        highlight1 = Highlight("test")
        highlight2 = Highlight("test")
        assert highlight1 == highlight2


class TestMarker:
    def test_from_bytes(self):
        file = b"test"
        marker = Marker.from_bytes(file)
        assert marker.file == file

    def test_from_disk(self, tmp_path):
        path = tmp_path / "test.pdf"
        path.write_bytes(b"test")
        marker = Marker.from_disk(path)
        assert marker.file == b"test"
        assert marker.path == path

    def test_add(self):
        marker = Marker(b"test")
        highlight = Highlight("test")
        marker.add(highlight)
        assert marker.highlights == set([highlight])

    def test_mark(self):
        marker = Marker.from_disk(path="tests/data/test.pdf")
        marker.add(Highlight("sample"))
        marker.add(Highlight("con", color=Colors.red, subwords=True))
        marker.add(
            [
                Highlight("simple", color=Colors.cyan),
                Highlight("mauris", color=Colors.purple),
            ]
        )
        marker.add(Highlight("vivamus", color=Colors.pink, group="test"))
        marked_file = marker.to_bytes()

        assert md5(marker.file).hexdigest() != md5(marked_file).hexdigest()

    def test_to_disk(self, tmp_path):
        marker = Marker.from_disk(path="tests/data/test.pdf")
        marker.add(Highlight("sample"))
        marker.to_disk(path=tmp_path / "marked.pdf")

    def test_highlight_with_group(self):
        highlight = Highlight("test", group="group1")
        assert highlight.text == "test"
        assert highlight.group == "group1"

    def test_highlight_with_subwords(self):
        highlight = Highlight("test", subwords=True)
        assert highlight.text == "test"
        assert highlight.subwords is True

    def test_marker_to_disk(self, tmp_path):
        marker = Marker.from_disk(path="tests/data/test.pdf")
        marker.add(Highlight("sample"))
        marker.to_disk(path=tmp_path / "marked.pdf")
        assert (tmp_path / "marked.pdf").exists()
