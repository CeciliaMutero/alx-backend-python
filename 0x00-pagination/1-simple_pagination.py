#!/usr/bin/env python3
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes for the given page and page size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Caches and returns the dataset loaded from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of the dataset.

        Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, (
            "page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be a positive integer"
        )
        start, end = index_range(page, page_size)

        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
