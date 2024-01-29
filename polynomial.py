class Expression:
    def __init__(self, tier, op=None):
        self.tier = tier
        self.op = op

    def __repr__(self):
        if self.p1.tier < self.tier:
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)
        
        if self.p2.tier < self.tier:
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)

        return left + " " + self.op + " " + right

class X(Expression):
    def __init__(self):
        super().__init__(3)

    def __repr__(self):
        return "X"

class Int(Expression):
    def __init__(self, i):
        super().__init__(3)
        self.i = i
    
    def __repr__(self):
        return str(self.i)


class Add(Expression):
    def __init__(self, p1, p2):
        super().__init__(1, "+")
        self.p1 = p1
        self.p2 = p2

class Sub(Expression):
    def __init__(self, p1, p2):
        super().__init__(1, "-")
        self.p1 = p1
        self.p2 = p2

class Mul(Expression):
    def __init__(self, p1, p2):
        super().__init__(2, "*")
        self.p1 = p1
        self.p2 = p2

class Div(Expression):
    def __init__(self, p1, p2):
        super().__init__(2, "/")
        self.p1 = p1
        self.p2 = p2


def test_given_test():
    poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
    answer = "4 + 3 + X + 1 * ( X * X + 1 )"

    assert repr(poly) == answer

def test_mul():
    poly = Mul( X(), Int(5) )
    answer = "X * 5"

    assert repr(poly) == answer

def test_div():
    poly = Div( X(), Int(5) )
    answer = "X / 5"

    assert repr(poly) == answer

def test_all_add():
    poly = Add( Add ( Add ( Int(4), Int(5) ), X() ), Add( Int(5), Int(10)))
    answer = "4 + 5 + X + 5 + 10"

    assert repr(poly) == answer

def test_alternate_three_times():
    poly = Add( Div( Add( Int(5), Int(3) ), Add( Int(7), Int(9) ) ), Int(3))
    answer = "( 5 + 3 ) / ( 7 + 9 ) + 3"

    assert repr(poly) == answer

def test_all_four():
    poly = Add( Div( Int(4), Sub( Int(3), X() )), Mul( Int(3), Int(8)))
    answer = "4 / ( 3 - X ) + 3 * 8"

    assert repr(poly) == answer