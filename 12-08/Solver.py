class Solver:

    def __init__(self):
        # instantiate every segment with all possible segment-options.
        self.a = list("abcdefg")
        self.b = list("abcdefg")
        self.c = list("abcdefg")
        self.d = list("abcdefg")
        self.e = list("abcdefg")
        self.f = list("abcdefg")
        self.g = list("abcdefg")

    def __str__(self):
        res = ""
        res += f"A could be any of: {self.a}\n" if len(self.a) > 1 else f"A is {self.a[0]}\n"
        res += f"B could be any of: {self.b}\n" if len(self.b) > 1 else f"B is {self.b[0]}\n"
        res += f"C could be any of: {self.c}\n" if len(self.c) > 1 else f"C is {self.c[0]}\n"
        res += f"D could be any of: {self.d}\n" if len(self.d) > 1 else f"D is {self.d[0]}\n"
        res += f"E could be any of: {self.e}\n" if len(self.e) > 1 else f"E is {self.e[0]}\n"
        res += f"F could be any of: {self.f}\n" if len(self.f) > 1 else f"F is {self.f[0]}\n"
        res += f"G could be any of: {self.g}" if len(self.g) > 1 else f"G is {self.g[0]}"
        return res

    def interpret_segment(self, segment):
        """
        We don't know which element of a segment is connected to which,
        but we can reduce the number of options based on the input!

        1, 4, 7, and 8 each use a unique number of segments and we can say exactly which segments are used.
        [2,3,5] all have 5 highlighted segments and commonly use the segments [a, d, g].
        [0,6,9] all have 6 highlighted segments and commonly use the segments [a, b, f, g].

        For each length of segment we can thus reduce the possible mapping-options of a specific letter.
        """
        if len(segment) == 2:  # must be a one
            # the two letters in here MUST be connected to ["c", "f"]
            self.c = list(set(self.c) & set(list(segment)))
            self.f = list(set(self.f) & set(list(segment)))
        elif len(segment) == 3:   # must be a seven
            # the three letters in here MUST be connected to ["a", "c", "f"]
            self.a = list(set(self.a) & set(list(segment)))
            self.c = list(set(self.c) & set(list(segment)))
            self.f = list(set(self.f) & set(list(segment)))
        elif len(segment) == 4:   # must be a four
            # the four letters in here MUST be connected to ["b", "c", "d", "f"]
            self.b = list(set(self.b) & set(list(segment)))
            self.c = list(set(self.c) & set(list(segment)))
            self.d = list(set(self.d) & set(list(segment)))
            self.f = list(set(self.f) & set(list(segment)))
        elif len(segment) == 5:  # could be either one of [2, 3, 5]
            # 2, 3 and 5 all use the following segments: a, d, g  -> we can reduce their respective options!
            self.a = list(set(self.a) & set(list(segment)))
            self.d = list(set(self.d) & set(list(segment)))
            self.g = list(set(self.g) & set(list(segment)))
        elif len(segment) == 6:  # could be either one of [0, 9, 6]
            # 0, 9 and 6 all use the following segments: a, b, f, g -> we can reduce their respective options!
            self.a = list(set(self.a) & set(list(segment)))
            self.b = list(set(self.b) & set(list(segment)))
            self.f = list(set(self.f) & set(list(segment)))
            self.g = list(set(self.g) & set(list(segment)))
        elif len(segment) == 7:   # must be an eight
            # the 7 letters in here are connected to all -> no reducing of options possible.
            pass

    def clean_solutions(self):
        """
        If a mapping is 1:1, we can remove the mapped value from all other lists of possible options.
        By doing this we reduce all lists until for each segment only one mapped value is left.
        """
        while True:
            for options in [self.a, self.b, self.c, self.d,  self.e, self.f, self.g]:
                if len(options) == 1:
                    # remove option from all other segments as it has to be the one with the only possibility.
                    for inner in [self.a, self.b, self.c, self.d,  self.e, self.f, self.g]:
                        if options != inner and options[0] in inner:
                            inner.remove(options[0])

            if max([len(x) for x in [self.a, self.b, self.c, self.d,  self.e, self.f, self.g]]) == 1:
                # Iterate until all only have 1 valid option.
                break

    def decode(self, letters):
        """
        Receives a sequence of segments and uses the mapped values to translate it first into the actually
        highlighted segments.
        As a second step we decode the correct segments into numbers.
        """
        # Translate with the mapping lists - the lists only contain exactly 1 letter.
        actual_segments = []
        for letter in letters:
            if letter in self.a:
                actual_segments.append("a")
            elif letter in self.b:
                actual_segments.append("b")
            elif letter in self.c:
                actual_segments.append("c")
            elif letter in self.d:
                actual_segments.append("d")
            elif letter in self.e:
                actual_segments.append("e")
            elif letter in self.f:
                actual_segments.append("f")
            elif letter in self.g:
                actual_segments.append("g")

        # Translate the segments into the correct number.
        actual_segments.sort()
        actual_segments = ''.join(actual_segments)
        if actual_segments == 'abcdfg':
            return 9
        elif actual_segments == 'abcdefg':
            return 8
        elif actual_segments == 'acf':
            return 7
        elif actual_segments == 'abdefg':
            return 6
        elif actual_segments == 'abdfg':
            return 5
        elif actual_segments == 'bcdf':
            return 4
        elif actual_segments == 'acdfg':
            return 3
        elif actual_segments == 'acdeg':
            return 2
        elif actual_segments == 'cf':
            return 1
        elif actual_segments == 'abcefg':
            return 0

        raise ValueError("Could not decode into a valid segment.")
