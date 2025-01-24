# import logging
# import logging.config
# import os
# from datetime import datetime
#
# from pydantic import BaseModel
#
# from pythonjsonlogger import jsonlogger
#
#
# class LogConfig(BaseModel):
#     """
#     Logging configuration
#     """
#
#     LOGGER_NAME: str = "root"
#     LOG_FORMATTER_STRING: str = "%(levelname)s | %(asctime)s | %(message)s"
#     LOG_LEVEL: str = "INFO"
#
#     # Logging config
#     # version = 1
#     # disable_existing_loggers = True
#     formatters = {
#         "JSON": {
#             "()": "skyvafnir_network_test.log_config.JsonFormatter.create",
#             "fmt": LOG_FORMATTER_STRING,
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         }
#     }
#     handlers = {
#         "JSON": {
#             "formatter": "JSON",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stdout",
#         },
#     }
#     loggers = {
#         "root": {"handlers": ["JSON"], "level": LOG_LEVEL},
#     }
#
#
# # This field is added by Uvicorn but we don't want to include it.
# delete_fields = ("color_message",)
#
#
# def _delete_fields(rec):
#     for key in delete_fields:
#         if key in rec:
#             del rec[key]
#
#
# class JsonFormatter(jsonlogger.JsonFormatter):
#     def add_fields(self, log_record, record, message_dict):
#         super().add_fields(log_record, record, message_dict)
#         _delete_fields(log_record)
#         log_record["timestamp"] = datetime.now().isoformat(timespec="milliseconds")
#
#     @classmethod
#     def create(cls, *args, **kwargs):
#         kwargs["rename_fields"] = {"levelname": "level", "exc_info": "exception"}
#         kwargs["json_indent"] = 2 if "local" in os.environ.get("VERSION", "local") else None
#         logging.captureWarnings(True)
#         return cls(*args, **kwargs)
#
#
def configure_logging(log_format: str = "JSON", log_level: str = "INFO"):
    return
#     if log_format.upper() == "JSON":
#         log_config = LogConfig()
#         log_config.loggers = {
#             "root": {"handlers": ["JSON"], "level": log_level},
#         }
#         logging.config.dictConfig(log_config.dict())
#     else:  # PLAINTEXT logging
#         log_handler = logging.StreamHandler()
#         logging.basicConfig(level=log_level.upper(), handlers=[log_handler])
