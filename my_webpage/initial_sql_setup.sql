--Initial SQL setup for store messages
--Log Table
CREATE TABLE IF NOT EXISTS public.logs
(
    "Id" integer NOT NULL DEFAULT nextval('"logs_Id_seq"'::regclass),
    date timestamp without time zone,
    app text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    status text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.logs
    OWNER to postgres;
--Message Table
