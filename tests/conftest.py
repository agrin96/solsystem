import pytest

@pytest.fixture(scope = "session")
def solana_endpoint() -> str:
	return "https://api.mainnet-beta.solana.com"



@pytest.fixture(scope = "session")
def helius_endpoint() -> str:
	raise RuntimeError("Need to set your own URL")
	return ""



@pytest.fixture(scope = "session")
def helius_wsendpoint() -> str:
	raise RuntimeError("Need to set your own URL")
	return ""
