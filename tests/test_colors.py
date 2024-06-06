from pdfmarker.colors import Color, Colors


def test_color_hash():
    color = Color("#f87171")
    assert hash(color) == hash(color.rgb)


def test_color_rgb():
    color = Color("#f87171")
    assert color._rgb("#f87171") == (248 / 255, 113 / 255, 113 / 255)


def test_colors_exist():
    assert hasattr(Colors, "red")
    assert hasattr(Colors, "orange")
    assert hasattr(Colors, "yellow")
    assert hasattr(Colors, "lime")
    assert hasattr(Colors, "green")
    assert hasattr(Colors, "emerald")
    assert hasattr(Colors, "teal")
    assert hasattr(Colors, "cyan")
    assert hasattr(Colors, "sky")
    assert hasattr(Colors, "blue")
    assert hasattr(Colors, "indigo")
    assert hasattr(Colors, "violet")
    assert hasattr(Colors, "purple")
    assert hasattr(Colors, "fuchsia")
    assert hasattr(Colors, "pink")
    assert hasattr(Colors, "rose")


def test_colors_values():
    assert Colors.red.hex == "#f87171"
    assert Colors.orange.hex == "#fb923c"
    assert Colors.yellow.hex == "#facc15"
    assert Colors.lime.hex == "#a3e635"
    assert Colors.green.hex == "#4ade80"
    assert Colors.emerald.hex == "#34d399"
    assert Colors.teal.hex == "#2dd4bf"
    assert Colors.cyan.hex == "#22d3ee"
    assert Colors.sky.hex == "#38bdf8"
    assert Colors.blue.hex == "#60a5fa"
    assert Colors.indigo.hex == "#818cf8"
    assert Colors.violet.hex == "#a78bfa"
    assert Colors.purple.hex == "#c084fc"
    assert Colors.fuchsia.hex == "#e879f9"
    assert Colors.pink.hex == "#f472b6"
    assert Colors.rose.hex == "#fb7185"
