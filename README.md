# 🏥 Verificador de Saúde de Sistemas Internos

Script Python com FastAPI que verifica o status de sistemas internos de forma assíncrona — todos ao mesmo tempo, não um por um — e retorna um relatório de saúde em JSON.

## 🔍 O que o script faz

- Simula sistemas internos (RH, Autenticação, Backup)
- Verifica todos simultaneamente usando async/await
- Expõe uma API REST com documentação automática

## ▶️ Como executar

```bash
pip install fastapi uvicorn
uvicorn verificador:app --reload
```

## 🌐 Acesse no navegador

| O quê | Endereço |
|---|---|
| 📊 Relatório | http://127.0.0.1:8000/saude |
| 📚 Documentação | http://127.0.0.1:8000/docs |