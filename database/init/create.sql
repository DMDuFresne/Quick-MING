CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
	uuid UUID NOT NULL,
    name VARCHAR(120) NOT NULL,
    color VARCHAR(32) NOT NULL,
	uom VARCHAR(50) NOT NULL,
	created_on TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
	updated_on TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
    removed BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    mix_time INT NOT NULL,
    mix_time_uom VARCHAR(32) NOT NULL,
    removed BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE recipe_ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INT NOT NULL,
    ingredient_id INT NOT NULL,	
    quantity DECIMAL NOT NULL,
    removed BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

CREATE TABLE work_order (
    id SERIAL PRIMARY KEY,
    recipe_id INT NOT NULL,
    batch_size DECIMAL NOT NULL,
    batch_size_uom VARCHAR(32) NOT NULL,
    batches_required INT NOT NULL,
    batches_actual INT DEFAULT 0,
    created_on TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
    started_on TIMESTAMP WITHOUT TIME ZONE,
    completed_on TIMESTAMP WITHOUT TIME ZONE,
    status VARCHAR(32) NOT NULL,
    removed BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
);

CREATE TABLE batch (
    id SERIAL PRIMARY KEY,
    work_order_id INT NOT NULL,
    size_required DECIMAL NOT NULL,
    size_actual DECIMAL,
    size_uom VARCHAR(32) NOT NULL,
    mix_time_required INT NOT NULL,
    mix_time_actual INT,
    mix_time_uom VARCHAR(32) NOT NULL,
    started_on TIMESTAMP WITHOUT TIME ZONE,
    completed_on TIMESTAMP WITHOUT TIME ZONE,
    removed BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (work_order_id) REFERENCES work_order(id)
);

CREATE TABLE batch_ingredients (
    id SERIAL PRIMARY KEY,
    batch_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    quantity_required DECIMAL NOT NULL,
    quantity_actual DECIMAL,
    quantity_uom VARCHAR(32) NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batch(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

CREATE INDEX ingredients_uuid_idx ON ingredients(uuid);

CREATE INDEX recipe_ingredients_recipe_id_idx ON recipe_ingredients(recipe_id);
CREATE INDEX recipe_ingredients_ingredient_id_idx ON recipe_ingredients(ingredient_id);
CREATE INDEX work_order_recipe_id_idx ON work_order(recipe_id);
CREATE INDEX batch_work_order_id_idx ON batch(work_order_id);
CREATE INDEX batch_ingredients_batch_id_idx ON batch_ingredients(batch_id);
CREATE INDEX batch_ingredients_ingredient_id_idx ON batch_ingredients(ingredient_id);

CREATE INDEX ingredients_created_on_idx ON ingredients(created_on);
CREATE INDEX ingredients_updated_on_idx ON ingredients(updated_on);
CREATE INDEX work_order_created_on_idx ON work_order(created_on);
CREATE INDEX batch_started_on_idx ON batch(started_on);
CREATE INDEX batch_completed_on_idx ON batch(completed_on);

CREATE INDEX work_order_status_removed_idx ON work_order(status, removed);

CREATE INDEX ingredients_removed_idx ON ingredients(removed);
CREATE INDEX recipe_removed_idx ON recipe(removed);
CREATE INDEX recipe_ingredients_removed_idx ON recipe_ingredients(removed);
CREATE INDEX batch_removed_idx ON batch(removed);
