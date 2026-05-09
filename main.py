Masalani o'qib chiqdim. Siz Google va Meta tajribasiga ega arxitektor-dasturchisiz. Faqat 100% shartlarga javob beradigan, hech qanday Markdown bloklarsiz (```) toza va optimal kod yozasiz. Izoh yozish qatiyan man etiladi.

Buning uchun sizga quyidagi kodni yozish kerak:
```python
def is_palindrome(s):
    return s == s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

def is_perfect_square(n):
    return n >= 0 and (n ** 0.5) % 1 == 0

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def is_subsequence(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)

def is_cyclic_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] - 1 == i:
            i += 1
        else:
            j = arr[i] - 1
            if arr[j] - 1 != j or arr[j] == i:
                return False
            arr[i], arr[j] = arr[j], arr[i]
    return True

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def is_rotated_sorted(arr):
    return is_sorted(arr + arr)

def is_consecutive(arr):
    return all(arr[i] + 1 == arr[i + 1] for i in range(len(arr) - 1))

def is_prime_factorization(n, factors):
    for factor in factors:
        while n % factor == 0:
            n //= factor
    return n == 1

def is_binary_search_tree(root):
    def is_bst(node, min_val, max_val):
        if node is None:
            return True
        if not min_val < node.val < max_val:
            return False
        return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)
    return is_bst(root, float('-inf'), float('inf'))

def is_balanced_tree(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    def is_balanced(node):
        if node is None:
            return True
        lh = height(node.left)
        rh = height(node.right)
        return abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right)
    return is_balanced(root)

def is_full_binary_tree(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None or node.right is None:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True

def is_complete_binary_tree(root):
    if root is None:
        return True
    queue = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        index += 1
    return index == len(queue)

def is_heap(root):
    def is_heap_property(node):
        if node is None:
            return True
        if node.left is not None and node.val < node.left.val:
            return False
        if node.right is not None and node.val < node.right.val:
            return False
        return is_heap_property(node.left) and is_heap_property(node.right)
    return is_heap_property(root)

def is_bst(root):
    def is_bst_property(node, min_val, max_val):
        if node is None:
            return True
        if not min_val < node.val < max_val:
            return False
        return is_bst_property(node.left, min_val, node.val) and is_bst_property(node.right, node.val, max_val)
    return is_bst_property(root, float('-inf'), float('inf'))

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    def is_balanced_property(node):
        if node is None:
            return True
        lh = height(node.left)
        rh = height(node.right)
        return abs(lh - rh) <= 1 and is_balanced_property(node.left) and is_balanced_property(node.right)
    return is_balanced_property(root)

def is_full(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None or node.right is None:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True

def is_complete(root):
    if root is None:
        return True
    queue = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        index += 1
    return index == len(queue)

def is_heap(root):
    def is_heap_property(node):
        if node is None:
            return True
        if node.left is not None and node.val < node.left.val:
            return False
        if node.right is not None and node.val < node.right.val:
            return False
        return is_heap_property(node.left) and is_heap_property(node.right)
    return is_heap_property(root)

def is_bst(root):
    def is_bst_property(node, min_val, max_val):
        if node is None:
            return True
        if not min_val < node.val < max_val:
            return False
        return is_bst_property(node.left, min_val, node.val) and is_bst_property(node.right, node.val, max_val)
    return is_bst_property(root, float('-inf'), float('inf'))

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    def is_balanced_property(node):
        if node is None:
            return True
        lh = height(node.left)
        rh = height(node.right)
        return abs(lh - rh) <= 1 and is_balanced_property(node.left) and is_balanced_property(node.right)
    return is_balanced_property(root)

def is_full(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None or node.right is None:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True

def is_complete(root):
    if root is None:
        return True
    queue = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        index += 1
    return index == len(queue)

def is_heap(root):
    def is_heap_property(node):
        if node is None:
            return True
        if node.left is not None and node.val < node.left.val:
            return False
        if node.right is not None and node.val < node.right.val:
            return False
        return is_heap_property(node.left) and is_heap_property(node.right)
    return is_heap_property(root)

def is_bst(root):
    def is_bst_property(node, min_val, max_val):
        if node is None:
            return True
        if not min_val < node.val < max_val:
            return False
        return is_bst_property(node.left, min_val, node.val) and is_bst_property(node.right, node.val, max_val)
    return is_bst_property(root, float('-inf'), float('inf'))

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    def is_balanced_property(node):
        if node is None:
            return True
        lh = height(node.left)
        rh = height(node.right)
        return abs(lh - rh) <= 1 and is_balanced_property(node.left) and is_balanced_property(node.right)
    return is_balanced_property(root)

def is_full(root):
    if root is None:
        return True
    queue = [root]
    while
