@dataclass(frozen=True)
class Pixel:

    row: int

    col: int

    x: float

    y: float

    values: np.ndarray