# MLOps

Студент: Слободчиков Дмитрий Алексеевич
Группа: РИМ-230971

## Установка

1. Установить зависимости через Poetry:
   ```bash
   poetry install --no-root
   ```
2. Запустить контейнер Docker с minio:
   ```bash
   docker-compose up -d        
   ```
3. Установить права доступа:
   ```bash
   chmod +x src/modeling/shell/*.sh pipeline.sh preparation.sh src/shell/*.sh full_pipeline.sh
   ```
4. Установка pre-commit:
   ```bash
   pre-commit install
   ```
   
5. Запустить pipeline.sh:
   ```bash
   ./pipeline_train.sh
   ```