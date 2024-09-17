from pydantic_settings import BaseSettings

class Settings(BaseSettings):


    # True - вкл
    # False - выкл

    TAPS_ENABLED: bool = True
    TAPS_PER_SECOND: list[int] = [20, 30]  # tested with 4 fingers
    INVEST_ENABLED: bool = False  # НЕ ВОРК
    PVP_ENABLED: bool = False # ПОКА ЧТО НЕ ВОРК будет работать после прокачки навыка "переговоры"
    PVP_LEAGUE: str = 'auto'
    PVP_UPGRADE_LEAGUE: bool = True
    PVP_COUNT: int = 10
    PVP_STRATEGY: str = 'random'
    SKILLS_COUNT: int = 10
    SKILLS_MODE: str = 'aggressive'
    IGNORED_SKILLS: list[str] = []
    MINING_SKILLS_LEVEL: int = 10
    PROTECTED_BALANCE: int = 0


    SLEEP_BETWEEN_START: list[int] = [1, 2]


try:
    config = Settings()
except Exception as error:
    print(f"{error}")
    config = False
