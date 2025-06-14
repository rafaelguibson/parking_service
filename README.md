# 🚗 Sistema de Controle de Estacionamento

Este projeto é um sistema de controle de estacionamento desenvolvido em Django, com foco na gestão de clientes, veículos, tipos de veículos, vagas e registros de estacionamento.

## 📌 Modelagem do Sistema

### 1. Customer
Representa um cliente do estacionamento.

- **id**: Chave primária (`int`)
- **user**: Chave estrangeira `OneToOne` para o modelo `User` do Django
- **cpf**: Campo de texto (`CharField`) para CPF do cliente

### 2. VehicleType
Tipo do veículo (carro, moto, etc).

- **id**: Chave primária (`int`)
- **type**: Nome do tipo de veículo (`CharField`)

### 3. Vehicle
Representa um veículo registrado.

- **id**: Chave primária (`int`)
- **owner**: Chave estrangeira para `Customer`
- **type**: Chave estrangeira para `VehicleType`

### 4. ParkingSpot
Define uma vaga no estacionamento.

- **id**: Chave primária (`int`)
- **spot**: Identificação da vaga (`CharField`)
- **is_occupied**: Indicador booleano de ocupação

### 5. ParkingRecord
Registra o uso da vaga por um veículo.

- **id**: Chave primária (`int`)
- **vehicle**: Chave estrangeira para `Vehicle`
- **parking_spot**: Chave estrangeira para `ParkingSpot`

## 🔗 Relacionamentos

- `Customer` possui uma relação `OneToOne` com `User` do Django.
- `Vehicle` possui chaves estrangeiras para `Customer` e `VehicleType`.
- `ParkingRecord` vincula um `Vehicle` a um `ParkingSpot`.

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/controle-estacionamento.git
   cd controle-estacionamento
