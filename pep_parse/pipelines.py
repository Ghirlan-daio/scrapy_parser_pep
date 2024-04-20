import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict()

    def process_item(self, item, spider):
        status = item["status"]
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        date = dt.datetime.now().strftime(DATETIME_FORMAT)
        filename = f"status_summary_{date}.csv"
        downloads_dir = results_dir / filename
        with open(downloads_dir, mode="w", encoding="utf-8") as f:
            writer = csv.writer(f, dialect="unix", quoting=csv.QUOTE_MINIMAL)
            total_statuses = sum(self.statuses.values())
            writer.writerows(
                [["Статус", "Количество"],
                 *self.statuses.items(),
                 ["Total", total_statuses]]
            )
