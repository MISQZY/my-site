class main:

    def __init__(self) -> None:
        self.level = 0

    def hurry(self):
        if self.level == 0:
            self.level = 1
            return 0
        elif self.level == 1:
            self.level = 2
            return 2
        elif self.level == 3:
            self.level = 4
            return 6
        else:
            raise KeyError()

    def mix(self):
        if self.level == 0:
            self.level = 2
            return 1
        elif self.level == 2:
            self.level = 3
            return 5
        elif self.level == 1:
            self.level = 4
            return 3
        else:
            raise KeyError()

    def rig(self):
        if self.level == 1:
            self.level = 5
            return 4
        elif self.level == 4:
            self.level = 5
            return 7
        elif self.level == 5:
            self.level = 3
            return 8
        else:
            raise KeyError()

o = main()
print(o.hurry()) # 0
print(o.hurry()) # 2
print(o.rig()) # KeyError
print(o.mix()) # 5
print(o.hurry()) # 6
print(o.rig()) # 7
print(o.rig()) # 8
print(o.hurry()) # 6
print(o.rig()) # 7
