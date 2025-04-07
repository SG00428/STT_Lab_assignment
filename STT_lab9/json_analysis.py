
# # Function to compute depths iteratively
# # def compute_depths(graph):
# #     depths = {mod: None for mod in graph}  # None = Unvisited
# #     stack = []  # Stack for DFS

# #     for mod in graph:
# #         if depths[mod] is not None:
# #             continue  # Already computed

# #         # Stack-based DFS to compute depth
# #         stack.append((mod, 1))  # (Module, Depth)

# #         while stack:
# #             node, depth = stack.pop()

# #             if depths[node] is not None and depths[node] >= depth:
# #                 continue  # Already visited with equal or greater depth

# #             depths[node] = depth  # Set depth

# #             for dep in graph.get(node, []):
# #                 if dep in graph:  # Only process known dependencies
# #                     stack.append((dep, depth + 1))

# #     return depths

# # # Compute depths
# # module_depths = compute_depths(dependency_graph)

# # # Print depth results
# # print("\n **Module Depth Analysis**\n")
# # print(f"{'Module':<50} {'Depth'}")
# # print("=" * 60)
# # for mod, depth in sorted(module_depths.items(), key=lambda x: x[1], reverse=True):
# #     print(f"{mod:<50} {depth}")


######################################

import json
from collections import defaultdict

json_file = r"C:\Users\Sneha Gautam\Downloads\stt_lab9\gym\dependencies.json"
with open(json_file, "r", encoding="utf-16") as f:
    dependencies = json.load(f)

dependency_graph = {mod: set(details.get("imports", [])) for mod, details in dependencies.items()}
fan_in = defaultdict(int)
fan_out = {mod: len(deps) for mod, deps in dependency_graph.items()}

# fan-in counts
for mod, imported_modules in dependency_graph.items():
    for imp in imported_modules:
        fan_in[imp] += 1

print("\n **Dependency Analysis**\n")
print(f"{'Module':<50} {'Fan-in':<10} {'Fan-out'}")
print("=" * 70)
for mod in dependency_graph:
    print(f"{mod:<50} {fan_in[mod]:<10} {fan_out[mod]}")

# Detect cycles in the graph
def detect_cycles(graph):
    visited, stack = set(), set()
    
    def visit(module):
        if module in stack:
            return [module]  # Cycle detected
        if module in visited:
            return []
        
        visited.add(module)
        stack.add(module)
        
        for dep in graph.get(module, []):
            cycle = visit(dep)
            if cycle:
                cycle.append(module)
                return cycle
        
        stack.remove(module)
        return []
    
    for mod in graph:
        cycle = visit(mod)
        if cycle:
            print("Cyclic Dependency Detected:", " → ".join(reversed(cycle)))

print("\n **Cyclic Dependency**\n")
detect_cycles(dependency_graph)

# core modules with high fan-in
core_modules = sorted(fan_in.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n Top 5 Core Modules (High Fan-In):")
for module, count in core_modules:
    print(f"  {module} - Used by {count} modules")

# high-risk modules (high fan-in and fan-out)
risk_modules = [(mod, fan_in[mod], fan_out[mod], fan_in[mod] * fan_out[mod]) for mod in dependency_graph]
risk_modules.sort(key=lambda x: x[3], reverse=True)

print("\n High-Risk Modules (Most Likely to Break System if Changed):")
print("-" * 50)
print(f"{'Module':40} {'Fan-In':8} {'Fan-Out':8} {'Risk Score'}")
print("-" * 50)
for module, fi, fo, score in risk_modules[:5]:
    print(f"{module:40} {fi:<8} {fo:<8} {score}")

# unused and disconnected modules
all_modules = set(dependency_graph.keys())
used_modules = {dep for deps in dependency_graph.values() for dep in deps}
unused_modules = all_modules - used_modules
disconnected_modules = {mod for mod in all_modules if not dependency_graph[mod]} & unused_modules

print("\n Unused Modules (Not Imported Anywhere):")
print("-" * 50)
for module in sorted(unused_modules):
    print(module)

print("\n Disconnected Modules (Isolated in the Graph):")
print("-" * 50)
for module in sorted(disconnected_modules):
    print(module)



def compute_depths_iterative(graph):
    depths = {}
    visited = set()

    for node in graph:
        if node in depths:
            continue

        stack = [(node, 1)]
        visiting = set()  # to avoid cycles

        while stack:
            current, depth = stack.pop()

            if current in depths:
                continue

            if current in visiting:
                continue  # no reprocessing

            visiting.add(current)
            children = graph.get(current, [])
            unvisited_children = [c for c in children if c not in depths and c in graph]

            if not unvisited_children:
                max_child_depth = max((depths.get(c, 0) for c in children if c in graph), default=0)
                depths[current] = 1 + max_child_depth
                visiting.remove(current)
                continue

            stack.append((current, depth))  # revisit later
            for c in unvisited_children:
                stack.append((c, depth + 1))

    return depths

module_depths = compute_depths_iterative(dependency_graph)

print("\n **Module Depth Analysis**\n")
print(f"{'Module':<50} {'Depth'}")
print("=" * 60)
for mod, depth in sorted(module_depths.items(), key=lambda x: x[1], reverse=True):
    print(f"{mod:<50} {depth}")
