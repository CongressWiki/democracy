CREATE FUNCTION public.set_current_timestamp_updated_at() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
  _new record;
BEGIN
  _new := NEW;
  _new."updated_at" = NOW();
  RETURN _new;
END;
$$;
CREATE TABLE public.bills (
    id text NOT NULL,
    type text NOT NULL,
    by_request jsonb NOT NULL,
    number integer NOT NULL,
    subject text NOT NULL,
    introduced_at timestamp with time zone DEFAULT now() NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    title text NOT NULL,
    summary text NOT NULL,
    status text NOT NULL,
    status_at timestamp with time zone DEFAULT now() NOT NULL,
    congress text NOT NULL,
    actions jsonb,
    sponsor text NOT NULL
);
CREATE TABLE public.committees (
    id text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    name text NOT NULL,
    description text NOT NULL
);
CREATE TABLE public.decisions (
    value text NOT NULL,
    comment text
);
CREATE TABLE public.elected_officials (
    id text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    service_start_at timestamp with time zone NOT NULL,
    service_end_at timestamp with time zone NOT NULL,
    member_id text NOT NULL,
    political_party_id text NOT NULL,
    state text NOT NULL,
    "position" text NOT NULL,
    rank text,
    senate_terms integer NOT NULL,
    house_terms integer NOT NULL,
    description text NOT NULL,
    is_active boolean NOT NULL,
    district integer
);
CREATE TABLE public.members (
    id text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    preferred_name text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    gender text NOT NULL,
    state text NOT NULL,
    image_url text,
    is_government_official boolean NOT NULL,
    political_party_id text NOT NULL,
    born_at timestamp with time zone NOT NULL
);
CREATE TABLE public.political_parties (
    id text DEFAULT public.gen_random_uuid() NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    name text NOT NULL,
    leading_member_id text NOT NULL,
    decision text NOT NULL
);
CREATE TABLE public.votes (
    id text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    bill_id text NOT NULL,
    member_id text NOT NULL,
    decision text NOT NULL
);
ALTER TABLE ONLY public.bills
    ADD CONSTRAINT bills_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.committees
    ADD CONSTRAINT committees_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.decisions
    ADD CONSTRAINT decisions_pkey PRIMARY KEY (value);
ALTER TABLE ONLY public.elected_officials
    ADD CONSTRAINT elected_officials_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.political_parties
    ADD CONSTRAINT political_parties_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.votes
    ADD CONSTRAINT votes_id_key UNIQUE (id);
ALTER TABLE ONLY public.votes
    ADD CONSTRAINT votes_pkey PRIMARY KEY (id);
CREATE TRIGGER set_public_committees_updated_at BEFORE UPDATE ON public.committees FOR EACH ROW EXECUTE FUNCTION public.set_current_timestamp_updated_at();
COMMENT ON TRIGGER set_public_committees_updated_at ON public.committees IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE TRIGGER set_public_elected_officials_updated_at BEFORE UPDATE ON public.elected_officials FOR EACH ROW EXECUTE FUNCTION public.set_current_timestamp_updated_at();
COMMENT ON TRIGGER set_public_elected_officials_updated_at ON public.elected_officials IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE TRIGGER set_public_members_updated_at BEFORE UPDATE ON public.members FOR EACH ROW EXECUTE FUNCTION public.set_current_timestamp_updated_at();
COMMENT ON TRIGGER set_public_members_updated_at ON public.members IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE TRIGGER set_public_political_parties_updated_at BEFORE UPDATE ON public.political_parties FOR EACH ROW EXECUTE FUNCTION public.set_current_timestamp_updated_at();
COMMENT ON TRIGGER set_public_political_parties_updated_at ON public.political_parties IS 'trigger to set value of column "updated_at" to current timestamp on row update';
