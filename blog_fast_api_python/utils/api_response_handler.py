from fastapi.responses import JSONResponse


from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_406_NOT_ACCEPTABLE, HTTP_409_CONFLICT, HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    HTTP_422_UNPROCESSABLE_ENTITY, HTTP_429_TOO_MANY_REQUESTS, HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE
)


class APIResponse:

    @staticmethod
    def HTTP_200_OK(data=None, message="Request successful"):
        return JSONResponse(
            content={
                "status": HTTP_200_OK, 
                "code": "HTTP_200_OK", 
                "message": message, 
                "data": data
            },
            status_code=HTTP_200_OK
        )

    @staticmethod
    def HTTP_201_CREATED(data=None, message="Resource created successfully"):
        return JSONResponse(
            content={"status": HTTP_201_CREATED, "code": "HTTP_201_CREATED", "message": message, "data": data},
            status_code=HTTP_201_CREATED
        )

    @staticmethod
    def HTTP_204_NO_CONTENT(message="No content", data=None):
        return JSONResponse(
            content={"status": HTTP_204_NO_CONTENT, "code": "HTTP_204_NO_CONTENT", "message": message, "data": data},
            status_code=HTTP_204_NO_CONTENT
        )

    @staticmethod
    def HTTP_400_BAD_REQUEST(message="Bad request", data=None):
        return JSONResponse(
            content={"status": HTTP_400_BAD_REQUEST, "code": "HTTP_400_BAD_REQUEST", "message": message, "data": data},
            status_code=HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def HTTP_401_UNAUTHORIZED(message="Unauthorized access", data=None):
        return JSONResponse(
            content={"status": HTTP_401_UNAUTHORIZED, "code": "HTTP_401_UNAUTHORIZED", "message": message, "data": data},
            status_code=HTTP_401_UNAUTHORIZED
        )

    @staticmethod
    def HTTP_403_FORBIDDEN(message="Permission denied", data=None):
        return JSONResponse(
            content={"status": HTTP_403_FORBIDDEN, "code": "HTTP_403_FORBIDDEN", "message": message, "data": data},
            status_code=HTTP_403_FORBIDDEN
        )

    @staticmethod
    def HTTP_404_NOT_FOUND(message="Resource not found", data=None):
        return JSONResponse(
            content={"status": HTTP_404_NOT_FOUND, "code": "HTTP_404_NOT_FOUND", "message": message, "data": data},
            status_code=HTTP_404_NOT_FOUND
        )

    @staticmethod
    def HTTP_409_CONFLICT(message="Resource conflict", data=None):
        return JSONResponse(
            content={"status": HTTP_409_CONFLICT, "code": "HTTP_409_CONFLICT", "message": message, "data": data},
            status_code=HTTP_409_CONFLICT
        )

    @staticmethod
    def HTTP_500_INTERNAL_SERVER_ERROR(message="Internal server error", data=None):
        return JSONResponse(
            content={"status": HTTP_500_INTERNAL_SERVER_ERROR, "code": "HTTP_500_INTERNAL_SERVER_ERROR", "message": message, "data": data},
            status_code=HTTP_500_INTERNAL_SERVER_ERROR
        )

    @staticmethod
    def HTTP_503_SERVICE_UNAVAILABLE(message="Service unavailable", data=None):
        return JSONResponse(
            content={"status": HTTP_503_SERVICE_UNAVAILABLE, "code": "HTTP_503_SERVICE_UNAVAILABLE", "message": message, "data": data},
            status_code=HTTP_503_SERVICE_UNAVAILABLE
        )

    @staticmethod
    def error(message="Internal server error", data=None):
        return JSONResponse(
            content={"status": HTTP_500_INTERNAL_SERVER_ERROR, "code": "HTTP_500_INTERNAL_SERVER_ERROR", "message": message, "data": data},
            status_code=HTTP_500_INTERNAL_SERVER_ERROR
        )

    @staticmethod
    def HTTP_405_METHOD_NOT_ALLOWED(message="Method not allowed", data=None):
        return JSONResponse(
            content={"status": HTTP_405_METHOD_NOT_ALLOWED, "code": "HTTP_405_METHOD_NOT_ALLOWED", "message": message, "data": data},
            status_code=HTTP_405_METHOD_NOT_ALLOWED
        )

    @staticmethod
    def HTTP_406_NOT_ACCEPTABLE(message="Not acceptable", data=None):
        return JSONResponse(
            content={"status": HTTP_406_NOT_ACCEPTABLE, "code": "HTTP_406_NOT_ACCEPTABLE", "message": message, "data": data},
            status_code=HTTP_406_NOT_ACCEPTABLE
        )

    @staticmethod
    def HTTP_415_UNSUPPORTED_MEDIA_TYPE(message="Unsupported media type", data=None):
        return JSONResponse(
            content={"status": HTTP_415_UNSUPPORTED_MEDIA_TYPE, "code": "HTTP_415_UNSUPPORTED_MEDIA_TYPE", "message": message, "data": data},
            status_code=HTTP_415_UNSUPPORTED_MEDIA_TYPE
        )

    @staticmethod
    def HTTP_429_TOO_MANY_REQUESTS(message="Too many requests", data=None):
        return JSONResponse(
            content={"status": HTTP_429_TOO_MANY_REQUESTS, "code": "HTTP_429_TOO_MANY_REQUESTS", "message": message, "data": data},
            status_code=HTTP_429_TOO_MANY_REQUESTS
        )

    @classmethod
    def HTTP_422_UNPROCESSABLE_ENTITY(cls, message="Unprocessable Entity", data=None):
        return JSONResponse(
            content={"status": HTTP_422_UNPROCESSABLE_ENTITY, "code": "HTTP_422_UNPROCESSABLE_ENTITY", "message": message, "data": data},
            status_code=HTTP_422_UNPROCESSABLE_ENTITY
        )
