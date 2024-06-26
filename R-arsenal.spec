#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-arsenal
Version  : 3.6.3
Release  : 26
URL      : https://cran.r-project.org/src/contrib/arsenal_3.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/arsenal_3.6.3.tar.gz
Summary  : An Arsenal of 'R' Functions for Large-Scale Statistical
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-knitr
BuildRequires : R-broom
BuildRequires : R-knitr
BuildRequires : R-pROC
BuildRequires : buildreq-R

%description
which are streamlined to work within the latest reporting tools in 'R' and
  'RStudio' and which use formulas and versatile summary statistics for summary
  tables and models. The primary functions include tableby(), a Table-1-like
  summary of multiple variable types 'by' the levels of one or more categorical
  variables; paired(), a Table-1-like summary of multiple variable types paired across
  two time points; modelsum(), which performs simple model fits on one or more endpoints
  for many variables (univariate or adjusted for covariates);
  freqlist(), a powerful frequency table across many categorical variables;
  comparedf(), a function for comparing data.frames; and
  write2(), a function to output tables to a document.

%prep
%setup -q -c -n arsenal
cd %{_builddir}/arsenal

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640971371

%install
export SOURCE_DATE_EPOCH=1640971371
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arsenal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arsenal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arsenal
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc arsenal || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/arsenal/DESCRIPTION
/usr/lib64/R/library/arsenal/INDEX
/usr/lib64/R/library/arsenal/Meta/Rd.rds
/usr/lib64/R/library/arsenal/Meta/data.rds
/usr/lib64/R/library/arsenal/Meta/features.rds
/usr/lib64/R/library/arsenal/Meta/hsearch.rds
/usr/lib64/R/library/arsenal/Meta/links.rds
/usr/lib64/R/library/arsenal/Meta/nsInfo.rds
/usr/lib64/R/library/arsenal/Meta/package.rds
/usr/lib64/R/library/arsenal/Meta/vignette.rds
/usr/lib64/R/library/arsenal/NAMESPACE
/usr/lib64/R/library/arsenal/NEWS.md
/usr/lib64/R/library/arsenal/R/arsenal
/usr/lib64/R/library/arsenal/R/arsenal.rdb
/usr/lib64/R/library/arsenal/R/arsenal.rdx
/usr/lib64/R/library/arsenal/data/Rdata.rdb
/usr/lib64/R/library/arsenal/data/Rdata.rds
/usr/lib64/R/library/arsenal/data/Rdata.rdx
/usr/lib64/R/library/arsenal/doc/comparedf.R
/usr/lib64/R/library/arsenal/doc/comparedf.Rmd
/usr/lib64/R/library/arsenal/doc/comparedf.html
/usr/lib64/R/library/arsenal/doc/freqlist.R
/usr/lib64/R/library/arsenal/doc/freqlist.Rmd
/usr/lib64/R/library/arsenal/doc/freqlist.html
/usr/lib64/R/library/arsenal/doc/index.html
/usr/lib64/R/library/arsenal/doc/labels.R
/usr/lib64/R/library/arsenal/doc/labels.Rmd
/usr/lib64/R/library/arsenal/doc/labels.html
/usr/lib64/R/library/arsenal/doc/modelsum.R
/usr/lib64/R/library/arsenal/doc/modelsum.Rmd
/usr/lib64/R/library/arsenal/doc/modelsum.html
/usr/lib64/R/library/arsenal/doc/paired.R
/usr/lib64/R/library/arsenal/doc/paired.Rmd
/usr/lib64/R/library/arsenal/doc/paired.html
/usr/lib64/R/library/arsenal/doc/tableby.R
/usr/lib64/R/library/arsenal/doc/tableby.Rmd
/usr/lib64/R/library/arsenal/doc/tableby.html
/usr/lib64/R/library/arsenal/doc/write2.R
/usr/lib64/R/library/arsenal/doc/write2.Rmd
/usr/lib64/R/library/arsenal/doc/write2.html
/usr/lib64/R/library/arsenal/help/AnIndex
/usr/lib64/R/library/arsenal/help/aliases.rds
/usr/lib64/R/library/arsenal/help/arsenal.rdb
/usr/lib64/R/library/arsenal/help/arsenal.rdx
/usr/lib64/R/library/arsenal/help/figures/logo.png
/usr/lib64/R/library/arsenal/help/paths.rds
/usr/lib64/R/library/arsenal/html/00Index.html
/usr/lib64/R/library/arsenal/html/R.css
/usr/lib64/R/library/arsenal/tests/testthat.R
/usr/lib64/R/library/arsenal/tests/testthat/helper-data.R
/usr/lib64/R/library/arsenal/tests/testthat/helper-script.R
/usr/lib64/R/library/arsenal/tests/testthat/mdat.rds
/usr/lib64/R/library/arsenal/tests/testthat/test_comparedf.R
/usr/lib64/R/library/arsenal/tests/testthat/test_formulize.R
/usr/lib64/R/library/arsenal/tests/testthat/test_freqlist.R
/usr/lib64/R/library/arsenal/tests/testthat/test_keep.labels.R
/usr/lib64/R/library/arsenal/tests/testthat/test_lhs_freqlist.R
/usr/lib64/R/library/arsenal/tests/testthat/test_lhs_modelsum.R
/usr/lib64/R/library/arsenal/tests/testthat/test_lhs_tableby.R
/usr/lib64/R/library/arsenal/tests/testthat/test_modelsum.R
/usr/lib64/R/library/arsenal/tests/testthat/test_paired.R
/usr/lib64/R/library/arsenal/tests/testthat/test_tableby.R
/usr/lib64/R/library/arsenal/tests/testthat/test_write2.R
/usr/lib64/R/library/arsenal/tests/testthat/write2.char.html.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.freqlist.doc.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.freqlist.html.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.lm.pdf.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.modelsum.html.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.multititles.pdf.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.mylist.pdf.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.mylist2.doc.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.mylists.pdf.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.render.html.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.tableby.html.Rmd
/usr/lib64/R/library/arsenal/tests/testthat/write2.yaml.pdf.Rmd
