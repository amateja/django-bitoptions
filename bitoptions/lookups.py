from django.db.models import Lookup


class BitwiseAnd(Lookup):
    """
    Custom lookup to determine whether a particular bit of a field is set or
    clear.
    """
    lookup_name = 'bitwise_and'

    def as_sql(self, compiler, connection):
        """
        Responsible for producing the query string and parameters for the
        expression.
        """
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '{0} & {1}'.format(lhs, rhs), params

    def as_postgresql(self, compiler, connection):
        """
        Works like as_sql() method but for PostgreSQL database.
        """
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '{0} & {1} > 0'.format(lhs, rhs), params
