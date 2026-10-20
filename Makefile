# Makefile — Build system for Story Project
# Supports: latexmk + xelatex, or tectonic

OUTDIR = output
AUXDIR = $(OUTDIR)/aux
LATEXMK := $(shell command -v latexmk 2>/dev/null)
TECTONIC := $(shell command -v tectonic 2>/dev/null)

.PHONY: all screenplay package one-pagers clean

define build_tex
	@mkdir -p $(OUTDIR) $(AUXDIR)
	@if [ -n "$(LATEXMK)" ]; then \
		cd $(1) && latexmk -xelatex -interaction=nonstopmode -halt-on-error \
			-outdir=../$(OUTDIR) -auxdir=../$(AUXDIR) $(2); \
	elif [ -n "$(TECTONIC)" ]; then \
		cd $(1) && tectonic --outdir ../$(OUTDIR) $(2); \
	else \
		echo "Error: no supported LaTeX builder found."; \
		echo "Install either latexmk + XeLaTeX or Tectonic."; \
		exit 127; \
	fi
endef

all: screenplay package one-pagers

# ============================================================
# SCREENPLAY
# ============================================================
screenplay: $(OUTDIR)/screenplay.pdf

$(OUTDIR)/screenplay.pdf: screenplay/main_screenplay.tex screenplay/*.tex common/*.tex
	$(call build_tex,screenplay,main_screenplay.tex)
	@mv $(OUTDIR)/main_screenplay.pdf $(OUTDIR)/screenplay.pdf 2>/dev/null || true

# ============================================================
# STUDIO PACKAGE
# ============================================================
package: $(OUTDIR)/studio-package.pdf

$(OUTDIR)/studio-package.pdf: package/studio_package.tex package/*.tex common/*.tex
	$(call build_tex,package,studio_package.tex)
	@mv $(OUTDIR)/studio_package.pdf $(OUTDIR)/studio-package.pdf 2>/dev/null || true

# ============================================================
# ONE-PAGERS
# ============================================================
one-pagers: $(OUTDIR)/one-pager.pdf $(OUTDIR)/actor-pitch.pdf $(OUTDIR)/director-pitch.pdf $(OUTDIR)/financier-pitch.pdf $(OUTDIR)/distributor-pitch.pdf $(OUTDIR)/producer-pitch.pdf $(OUTDIR)/festival-pitch.pdf $(OUTDIR)/streamer-pitch.pdf $(OUTDIR)/coproduction-pitch.pdf $(OUTDIR)/talent-rep-pitch.pdf $(OUTDIR)/awards-pitch.pdf $(OUTDIR)/public-funder-pitch.pdf $(OUTDIR)/exhibitor-pitch.pdf $(OUTDIR)/cultural-partnership-pitch.pdf $(OUTDIR)/press-pitch.pdf $(OUTDIR)/craft-pitch.pdf

$(OUTDIR)/one-pager.pdf: one_pagers/one_pager.tex common/*.tex
	$(call build_tex,one_pagers,one_pager.tex)
	@mv $(OUTDIR)/one_pager.pdf $(OUTDIR)/one-pager.pdf 2>/dev/null || true

$(OUTDIR)/actor-pitch.pdf: one_pagers/actor_pitch.tex common/*.tex
	$(call build_tex,one_pagers,actor_pitch.tex)
	@mv $(OUTDIR)/actor_pitch.pdf $(OUTDIR)/actor-pitch.pdf 2>/dev/null || true

$(OUTDIR)/director-pitch.pdf: one_pagers/director_pitch.tex common/*.tex
	$(call build_tex,one_pagers,director_pitch.tex)
	@mv $(OUTDIR)/director_pitch.pdf $(OUTDIR)/director-pitch.pdf 2>/dev/null || true

$(OUTDIR)/financier-pitch.pdf: one_pagers/financier_pitch.tex common/*.tex
	$(call build_tex,one_pagers,financier_pitch.tex)
	@mv $(OUTDIR)/financier_pitch.pdf $(OUTDIR)/financier-pitch.pdf 2>/dev/null || true

$(OUTDIR)/distributor-pitch.pdf: one_pagers/distributor_pitch.tex common/*.tex
	$(call build_tex,one_pagers,distributor_pitch.tex)
	@mv $(OUTDIR)/distributor_pitch.pdf $(OUTDIR)/distributor-pitch.pdf 2>/dev/null || true

$(OUTDIR)/producer-pitch.pdf: one_pagers/producer_pitch.tex common/*.tex
	$(call build_tex,one_pagers,producer_pitch.tex)
	@mv $(OUTDIR)/producer_pitch.pdf $(OUTDIR)/producer-pitch.pdf 2>/dev/null || true

$(OUTDIR)/festival-pitch.pdf: one_pagers/festival_pitch.tex common/*.tex
	$(call build_tex,one_pagers,festival_pitch.tex)
	@mv $(OUTDIR)/festival_pitch.pdf $(OUTDIR)/festival-pitch.pdf 2>/dev/null || true

$(OUTDIR)/streamer-pitch.pdf: one_pagers/streamer_pitch.tex common/*.tex
	$(call build_tex,one_pagers,streamer_pitch.tex)
	@mv $(OUTDIR)/streamer_pitch.pdf $(OUTDIR)/streamer-pitch.pdf 2>/dev/null || true

$(OUTDIR)/coproduction-pitch.pdf: one_pagers/coproduction_pitch.tex common/*.tex
	$(call build_tex,one_pagers,coproduction_pitch.tex)
	@mv $(OUTDIR)/coproduction_pitch.pdf $(OUTDIR)/coproduction-pitch.pdf 2>/dev/null || true

$(OUTDIR)/talent-rep-pitch.pdf: one_pagers/talent_rep_pitch.tex common/*.tex
	$(call build_tex,one_pagers,talent_rep_pitch.tex)
	@mv $(OUTDIR)/talent_rep_pitch.pdf $(OUTDIR)/talent-rep-pitch.pdf 2>/dev/null || true

$(OUTDIR)/awards-pitch.pdf: one_pagers/awards_pitch.tex common/*.tex
	$(call build_tex,one_pagers,awards_pitch.tex)
	@mv $(OUTDIR)/awards_pitch.pdf $(OUTDIR)/awards-pitch.pdf 2>/dev/null || true

$(OUTDIR)/public-funder-pitch.pdf: one_pagers/public_funder_pitch.tex common/*.tex
	$(call build_tex,one_pagers,public_funder_pitch.tex)
	@mv $(OUTDIR)/public_funder_pitch.pdf $(OUTDIR)/public-funder-pitch.pdf 2>/dev/null || true

$(OUTDIR)/exhibitor-pitch.pdf: one_pagers/exhibitor_pitch.tex common/*.tex
	$(call build_tex,one_pagers,exhibitor_pitch.tex)
	@mv $(OUTDIR)/exhibitor_pitch.pdf $(OUTDIR)/exhibitor-pitch.pdf 2>/dev/null || true

$(OUTDIR)/cultural-partnership-pitch.pdf: one_pagers/cultural_partnership_pitch.tex common/*.tex
	$(call build_tex,one_pagers,cultural_partnership_pitch.tex)
	@mv $(OUTDIR)/cultural_partnership_pitch.pdf $(OUTDIR)/cultural-partnership-pitch.pdf 2>/dev/null || true

$(OUTDIR)/press-pitch.pdf: one_pagers/press_pitch.tex common/*.tex
	$(call build_tex,one_pagers,press_pitch.tex)
	@mv $(OUTDIR)/press_pitch.pdf $(OUTDIR)/press-pitch.pdf 2>/dev/null || true

$(OUTDIR)/craft-pitch.pdf: one_pagers/craft_pitch.tex common/*.tex
	$(call build_tex,one_pagers,craft_pitch.tex)
	@mv $(OUTDIR)/craft_pitch.pdf $(OUTDIR)/craft-pitch.pdf 2>/dev/null || true

# ============================================================
# CLEAN
# ============================================================
clean:
	rm -rf $(OUTDIR)/*.pdf $(AUXDIR)
