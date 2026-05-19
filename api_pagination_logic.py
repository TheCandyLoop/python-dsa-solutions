import math

def paginate(items, page, page_size):

    total_items = len(items)
    total_pages = math.ceil(total_items / page_size)

    start = (page - 1) * page_size
    end = start + page_size

    paginated_data = items[start:end]

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_previous": page > 1,
        "data": paginated_data
    }


items = list(range(1, 51))

result = paginate(items, page=2, page_size=10)

print(result)
