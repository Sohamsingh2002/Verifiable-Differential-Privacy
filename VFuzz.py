import sqlparse
import re



class VFuzzCompiler:
    def __init__(self, privacy_budget=1.0):
        self.privacy_budget = privacy_budget

    def type_check_query(self, query):
        try:
            # Check if the query is well-formed
            self._check_well_formed(query)

            # Check if the query adheres to privacy budget
            self._check_privacy_budget(query)

            print("Query is differentially private and type-checked.")
        except Exception as e:
            print(f"Error: {e}")

    def _check_well_formed(self, query):
        # well-formedness check
        # Check if "map" and "split" are present in the query
        if "map" not in query and "split" not in query:
            raise ValueError("Query is not well-formed.")

    def _check_privacy_budget(self, query):
        # privacy budget check
        # Calculate the privacy cost of the query
        privacy_cost = self._calculate_privacy_cost(query)

        # Check if the privacy cost exceeds the budget
        if privacy_cost > self.privacy_budget:
            raise ValueError("Query exceeds privacy budget.")

    def _calculate_privacy_cost(self, query):
        

        # Assign privacy costs to different operations 
        operation_privacy_costs = {
            "map": 1,
            "count": 2,
            "split": 1,
            "sum": 2
        }

        # Calculate the privacy cost 
        privacy_cost = sum(operation_privacy_costs.get(op, 0) for op in query)

        return privacy_cost

    def convert_sql_to_vfuzz_query(self,sql_query):
    

      
        parsed_query = sqlparse.parse(sql_query)[0]

        
        vfuzz_query = []

       
        for token in parsed_query.tokens:
            vfuzz_operation = None 
            

            # Map SQL operations to VFuzz operations
            if token.normalized.lower() in {"select", "*"}:
                vfuzz_query.append("map")
            if re.match(r"^count\((.+)\)$", token.normalized.lower()):
                field_name = re.match(r"^count\((.+)\)$", token.normalized.lower()).group(1)
                vfuzz_query.append("count")
            if re.match(r"^avg\((.+)\)$", token.normalized.lower()):
                field_name = re.match(r"^avg\((.+)\)$", token.normalized.lower()).group(1)
                vfuzz_query.append("sum")  # Note: Using "sum" as suggested for "avg"
            if re.match(r"^where (.*)$", token.normalized.lower()):
                where_clause = re.match(r"^where (.*)$", token.normalized.lower()).group(1)
                vfuzz_query.append("split")

            
                

        return vfuzz_query


vfuzz_compiler = VFuzzCompiler(privacy_budget=5.0)


sql_query1 = "SELECT COUNT(*) FROM employees WHERE age > 25"
vfuzz_query1 = vfuzz_compiler.convert_sql_to_vfuzz_query(sql_query1)
print(vfuzz_query1)
vfuzz_compiler.type_check_query(vfuzz_query1)


sql_query2 = "SELECT AVG(salary) FROM employees WHERE department = 'IT'"
vfuzz_query2 = vfuzz_compiler.convert_sql_to_vfuzz_query(sql_query2)
print(vfuzz_query2)
vfuzz_compiler.type_check_query(vfuzz_query2)
