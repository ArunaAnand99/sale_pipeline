from src.utils.exceptions import(
PipelineError,
DataExtractionError,
DataQualityError,
DatabaseConnectionError
)

print("1. Catch specific error")
try:
    raise DataExtractionError("file not found")
except DataExtractionError as e:
    print(f"caught DataExtractionError:{e}")



print("2.catch child errors using parent:")
try:
    raise DataQualityError("data is not valid")
except PipelineError as e:
    print(f"caught pipelineerror :{e}")
    print(f"error tye:{type(e).__name__}")



print("3.multiple error ")
errors = [
    DataExtractionError("file not found"),
    DataQualityError("Data is not valid"),
    DatabaseConnectionError("can't connect to db")

]

for error in errors:
    try:
        raise error
    except PipelineError as e:
        print(f"caught:{type(e).__name__}")


print("4.finally block")
try:
    raise DatabaseConnectionError("db is down")
except DatabaseConnectionError as e:
    print(f" caught db error:{e}")
finally:
    print("finally block")


print("else block")
try:
    add = 1+2
except Exception as e:
    print(f"error:{e}")
else:
    print(f"succes:{add}")
finally:
    print("finally block")
    