def evaluate_expression(q, p, r):
    # Evaluate the given expression (~q v ~p v r) ^ (~q ^ p) ^ q
    expression_result = ((not q or not p or r) and (not q and p) and q)
    return expression_result

def generate_truth_table():
    # Print the header of the truth table
    print(" q | p | r | Expression (KB) | Query (r)")
    print("---|---|---|-----------------|------------")

    # Evaluate and print each row of the truth table
    for q in [True, False]:
        for p in [True, False]:
            for r in [True, False]:
                expression_result = evaluate_expression(q, p, r)
                query_result = r

                print(f" {q} | {p} | {r} | {expression_result}               | {query_result}")

def query_entails_knowledge():
    # Check if query entails the knowledge
    for q in [True, False]:
        for p in [True, False]:
            for r in [True, False]:
                expression_result = evaluate_expression(q, p, r)
                query_result = r

                # If the expression is true and the query is false, query does not entail the knowledge
                if expression_result and not query_result:
                    return False

    # If the loop completes without returning, query entails the knowledge
    return True

def main():
    # Generate and print the truth table
    generate_truth_table()

    # Check if query entails the knowledge and print the result
    if query_entails_knowledge():
        print("\nQuery entails the knowledge.")
    else:
        print("\nQuery does not entail the knowledge.")

if __name__ == "__main__":
    main()
