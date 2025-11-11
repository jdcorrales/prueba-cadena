# Etapa de build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

COPY ./src ./src
COPY ./tests ./tests

WORKDIR /app/src/PalindromoApp
RUN dotnet restore
RUN dotnet build -c Release

WORKDIR /app/tests/PalindromoApp.Tests
RUN dotnet restore
RUN dotnet build -c Release

# Etapa de test
FROM build AS test
WORKDIR /app/tests/PalindromoApp.Tests
CMD ["dotnet", "test", "--logger:trx"]
