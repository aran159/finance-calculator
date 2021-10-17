import attr


@attr.s(auto_attribs=True, kw_only=True)
class RegularInvestment:
    A: float = attr.ib()
    R: float = attr.ib()
    t0: float = attr.ib()
    Ta: float = attr.ib()


    @property
    def net_outcome(self):
        return self.A * (1 - self.t0) * (1 + self.R * (1 - self.Ta))


@attr.s(auto_attribs=True, kw_only=True)
class PensionScheme:
    A: float = attr.ib()
    R: float = attr.ib()
    t1: float = attr.ib()

    @property
    def net_outcome(self):
        return self.A * (1 + self.R) * (1 - self.t1)

    def t1_eq(self, t0: float, Ta: float):
        return (
            t0
            + (
                ((1 - t0) * self.R * Ta)
                / (1 + self.R)
            )
        )

    @property
    def relative_fiscal_profit(self, t0: float, Ta: float):
        return (
            (
                (1 - self.t1)
                / (1 - self.t1_eq(t0, Ta))
            )
            - 1
        )
