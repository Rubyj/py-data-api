from abc import ABC
from typing import Any, Type

from pydataapi.dbapi import Connection
from sqlalchemy.dialects.mysql.base import (
    MySQLCompiler,
    MySQLDDLCompiler,
    MySQLIdentifierPreparer,
    MySQLTypeCompiler,
)
from sqlalchemy.dialects.postgresql.base import (
    PGCompiler,
    PGDDLCompiler,
    PGIdentifierPreparer,
    PGInspector,
    PGTypeCompiler,
)
from sqlalchemy.engine.default import DefaultDialect


class DataAPIDialect(DefaultDialect, ABC):
    driver: str = 'dataapi'
    name = "mysql"
    supports_alter = True

    supports_native_boolean = True

    max_identifier_length = 255
    max_index_name_length = 64

    supports_native_enum = False

    supports_sane_rowcount = True
    supports_sane_multi_rowcount = False
    supports_multivalues_insert = True

    supports_comments = True
    inline_comments = True
    default_paramstyle = "named"

    cte_follows_insert = True

    statement_compiler = MySQLCompiler
    ddl_compiler = MySQLDDLCompiler
    type_compiler = MySQLTypeCompiler

    preparer = MySQLIdentifierPreparer

    _backslash_escapes = True
    _server_ansiquotes = False

    @property
    def _supports_cast(self) -> bool:
        return True

    @classmethod
    def dbapi(cls) -> Type[Connection]:
        return Connection

    def get_columns(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_primary_keys(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_foreign_keys(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_table_names(
        self, connection: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_temp_table_names(
        self, connection: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_view_names(
        self, connection: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_temp_view_names(
        self, connection: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_view_definition(
        self, connection: Any, view_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_indexes(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_unique_constraints(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_check_constraints(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def get_table_comment(
        self, connection: Any, table_name: Any, schema: Any = None, **kw: Any
    ) -> None:  # pragma: no cover
        pass

    def normalize_name(self, name: Any) -> None:  # pragma: no cover
        pass

    def denormalize_name(self, name: Any) -> None:  # pragma: no cover
        pass

    def has_table(
        self, connection: Any, table_name: Any, schema: Any = None
    ) -> None:  # pragma: no cover
        pass

    def has_sequence(
        self, connection: Any, sequence_name: Any, schema: Any = None
    ) -> None:  # pragma: no cover
        pass

    def _get_server_version_info(self, connection: Any) -> None:  # pragma: no cover
        pass

    def _get_default_schema_name(self, connection: Any) -> None:  # pragma: no cover
        pass

    def do_begin_twophase(self, connection: Any, xid: Any) -> None:  # pragma: no cover
        pass

    def do_prepare_twophase(
        self, connection: Any, xid: Any
    ) -> None:  # pragma: no cover
        pass

    def do_rollback_twophase(
        self, connection: Any, xid: Any, is_prepared: bool = True, recover: bool = False
    ) -> None:  # pragma: no cover
        pass

    def do_commit_twophase(
        self, connection: Any, xid: Any, is_prepared: bool = True, recover: bool = False
    ) -> None:  # pragma: no cover
        pass

    def do_recover_twophase(self, connection: Any) -> None:  # pragma: no cover
        pass

    def set_isolation_level(
        self, dbapi_conn: Any, level: Any
    ) -> None:  # pragma: no cover
        pass

    def get_isolation_level(self, dbapi_conn: Any) -> None:  # pragma: no cover
        pass


class MySQLDataAPIDialect(DataAPIDialect):
    name = "mysql"
    statement_compiler = MySQLCompiler
    ddl_compiler = MySQLDDLCompiler
    type_compiler = MySQLTypeCompiler

    preparer = MySQLIdentifierPreparer


class PostgreSQLDataAPIDialect(DataAPIDialect):
    name = "postgresql"
    supports_alter = True
    max_identifier_length = 63
    supports_sane_rowcount = True
    statement_compiler = PGCompiler
    ddl_compiler = PGDDLCompiler
    type_compiler = PGTypeCompiler
    preparer = PGIdentifierPreparer
    inspector = PGInspector
    isolation_level = None
