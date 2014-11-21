"""Tests the decorators."""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from sequential import before, after, during


__all__ = ['TestSequential']


class TestSequential(unittest.TestCase):
    def test_before_chain(self):
        """Tests @before chained to another function."""
        def add_b(word=''):
            return word + 'b'

        @before(add_b, chain=True)
        def add_a(word=''):
            return word + 'a'

        assert add_a() == 'ba'

    def test_before_no_chain(self):
        """Tests @before not chained to another function."""
        def switch_a(d):
            d['a'] = True

        @before(switch_a)
        def check_a(d):
            assert d['a']

        check_a({'a': False})

    def test_after_chain(self):
        """Tests @after chained to another function."""
        def add_a(word=''):
            return word + 'a'

        @after(add_a, chain=True)
        def add_b(word=''):
            return word + 'b'

        assert add_b() == 'ba'

    def test_after_no_chain(self):
        """Tests @after not chained to another function."""
        def check_a(d):
            assert d['a']
            d['b'] = True

        @after(check_a)
        def switch_a(d):
            d['a'] = True

        d = {'a': False, 'b': False}
        switch_a(d)
        assert d['b']

    # TODO Come up with a good way of testing @during.
