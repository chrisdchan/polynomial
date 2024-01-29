import pytest

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

    def evaluate(self, x):
        return x

class Int(Expression):
    def __init__(self, i):
        super().__init__(3)
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, _):
        return self.i


class Add(Expression):
    def __init__(self, p1, p2):
        super().__init__(1, "+")
        self.p1 = p1
        self.p2 = p2

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Sub(Expression):
    def __init__(self, p1, p2):
        super().__init__(1, "-")
        self.p1 = p1
        self.p2 = p2

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)

class Mul(Expression):
    def __init__(self, p1, p2):
        super().__init__(2, "*")
        self.p1 = p1
        self.p2 = p2

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div(Expression):
    def __init__(self, p1, p2):
        super().__init__(2, "/")
        self.p1 = p1
        self.p2 = p2

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)

def test_eval_add():
    poly = Add(Int(5), X())
    actual = poly.evaluate(2)
    expected = 7

    assert actual == expected

def test_eval_given():
    poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
    actual = poly.evaluate(-1)
    expected = 8

    assert actual == expected

def test_divide_by_zero():
    poly = Div( Int(10), Sub(X(), X()))
    
    with pytest.raises(ZeroDivisionError):
        poly.evaluate(10)


def test_repr_given_test_repr():
    poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
    answer = "4 + 3 + X + 1 * ( X * X + 1 )"

    assert repr(poly) == answer

def test_repr_mul():
    poly = Mul( X(), Int(5) )
    answer = "X * 5"

    assert repr(poly) == answer

def test_repr_div():
    poly = Div( X(), Int(5) )
    answer = "X / 5"

    assert repr(poly) == answer

def test_repr_all_add():
    poly = Add( Add ( Add ( Int(4), Int(5) ), X() ), Add( Int(5), Int(10)))
    answer = "4 + 5 + X + 5 + 10"

    assert repr(poly) == answer

def test_repr_alternate_three_times():
    poly = Add( Div( Add( Int(5), Int(3) ), Add( Int(7), Int(9) ) ), Int(3))
    answer = "( 5 + 3 ) / ( 7 + 9 ) + 3"

    assert repr(poly) == answer

def test_repr_all_four():
    poly = Add( Div( Int(4), Sub( Int(3), X() )), Mul( Int(3), Int(8)))
    answer = "4 / ( 3 - X ) + 3 * 8"

    assert repr(poly) == answer