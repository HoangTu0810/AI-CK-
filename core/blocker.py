import os
import datetime
from core.predictor import WebsitePredictor

class WebsiteBlocker:
    def __init__(self):
        self.predictor = WebsitePredictor()
        self.history = []

        # User-level blocked sites (no admin required)
        self.blocked_sites_file = os.path.join(os.path.expanduser("~"), "blocked_sites.txt")
        self.blocked_sites = self._load_blocked_sites()

        # Windows path (for reference, but not used without admin)
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.redirect_ip = "127.0.0.1"

    def _load_blocked_sites(self):
        if os.path.exists(self.blocked_sites_file):
            with open(self.blocked_sites_file, "r") as f:
                return set(line.strip() for line in f if line.strip())
        return set()

    def _save_blocked_sites(self):
        with open(self.blocked_sites_file, "w") as f:
            for site in sorted(self.blocked_sites):
                f.write(f"{site}\n")

    def normalize(self, url: str) -> str:
        url = url.strip().lower()
        url = url.replace("http://", "").replace("https://", "")
        url = url.replace("www.", "")
        return url.split("/")[0]

    #  BLOCK 
    def block_website(self, url: str):
        normalized = self.normalize(url)
        if normalized in self.blocked_sites:
            return f"Website {normalized} is already blocked."
        
        self.blocked_sites.add(normalized)
        self._save_blocked_sites()
        return f"Website {normalized} blocked successfully."

    #  UNBLOCK 
    def unblock_website(self, url: str):
        normalized = self.normalize(url)
        if normalized not in self.blocked_sites:
            return f"Website {normalized} is not blocked."
        
        self.blocked_sites.remove(normalized)
        self._save_blocked_sites()
        return f"Website {normalized} unblocked successfully."

    #  HÀM CHÍNH (AI + BLOCK)
    def enforce(self, url: str):
        normalized = self.normalize(url)
        decision = self.predictor.predict(normalized)

        if decision == "BLOCK":
            block_result = self.block_website(normalized)
            # Perhaps log the block result, but for now, just proceed

        self.history.append({
            "url": normalized,
            "decision": decision,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return decision

        if decision == "BLOCK":
            self.block_website(normalized)
            return "BLOCKED (AI detected dangerous site)"
        else:
            return "ALLOWED (Safe site)"

    def unblock(self, url: str):
        normalized = self.normalize(url)
        self.unblock_website(normalized)
        return "UNBLOCKED"