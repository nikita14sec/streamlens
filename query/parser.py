from query.ast import Select, Join


class Parser:

    def parse(self, sql):

        tokens = sql.replace(",", " ").split()

        table = tokens[tokens.index("FROM") + 1]
        node = Select(table)

        i = 0
        while i < len(tokens):

            if tokens[i] == "WHERE":
                node.where = (tokens[i+1], tokens[i+3])

            if tokens[i] == "JOIN":
                jtable = tokens[i+1]
                on = tokens.index("ON")
                node.joins.append(
                    Join(jtable, tokens[on+1], tokens[on+3])
                )

            i += 1

        return node