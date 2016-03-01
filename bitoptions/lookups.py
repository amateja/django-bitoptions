from django.db.models import Lookup


class BitwiseAnd(Lookup):
    lookup_name = 'bitwise_and'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '{0} & {1}'.format(lhs, rhs), params

    def as_postgresql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '{0} & {1} > 0'.format(lhs, rhs), params
