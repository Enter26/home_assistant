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

-- Table: public.web_messages

-- DROP TABLE public.web_messages;

CREATE TABLE IF NOT EXISTS public.web_messages
(
    "Id" integer NOT NULL DEFAULT nextval('"web_messages_Id_seq"'::regclass),
    date timestamp without time zone,
    language text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    message text COLLATE pg_catalog."default",
    status text COLLATE pg_catalog."default",
    CONSTRAINT web_messages_pkey PRIMARY KEY ("Id")
)

TABLESPACE pg_default;

ALTER TABLE public.web_messages
    OWNER to postgres;
