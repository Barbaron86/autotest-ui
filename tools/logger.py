import sys

from loguru import logger


def configure_logging() -> None:
    logger.remove()
    logger.configure(extra={"component": "AUTOTEST"})

    logger.level("TRACE", icon="🔍", color="<dim>")
    logger.level("DEBUG", icon="🐛", color="<dim>")
    logger.level("INFO", icon="💡", color="<cyan>")
    logger.level("SUCCESS", icon="✅", color="<green>")
    logger.level("WARNING", icon="⚠️", color="<yellow>")
    logger.level("ERROR", icon="❌", color="<red>")
    logger.level("CRITICAL", icon="🔥", color="<bold><red>")

    logger.add(
        sys.stderr,
        level="DEBUG",
        colorize=None,
        diagnose=False,
        format=(
            "<dim>{time:HH:mm:ss.SSS}</dim> | "
            "<level>{level.icon} {level: <8}</level> | "
            "<magenta>{extra[component]: <14}</magenta> | "
            "{message}"
        ),
    )
