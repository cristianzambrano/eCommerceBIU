import json
from fastmcp import FastMCP

with open("db.json", "r", encoding="utf-8") as f:
    data = json.load(f)

productos = data.get("productos", [])

mcp = FastMCP("JSON Productos MCP Server")

@mcp.tool
def listar_productos() -> list[dict]:
    """Devuelve la lista completa de productos desde el JSON."""
    return productos

@mcp.tool
def consultar_producto(producto_id: str) -> dict:
    """Busca un producto por su ID en el JSON."""
    for p in productos:
        if p["id"] == str(producto_id):
            return p
    return {"error": "Producto no encontrado"}

if __name__ == "__main__":
    mcp.run()
