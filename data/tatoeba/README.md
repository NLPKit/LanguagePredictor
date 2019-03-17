#  Tatoeba

## Dependencies

Run the following to install the `shuf` command on macOS:

```bash
brew install coreutils
```

You will also need the `fasttext` binary:

```bash
git clone git@github.com:facebookresearch/fastText.git
cd fastText
make
cp ./fasttext /usr/local/bin/
```

## Preparing the Data

```bash
wget http://downloads.tatoeba.org/exports/sentences.tar.bz2
bunzip2 sentences.tar.bz2
tar xvf sentences.tar
awk -F"\t" '{print"__label__"$2" "$3}' < sentences.csv | shuf > all.txt
head -n 10000 all.txt > valid.txt
tail -n +10001 all.txt > train.txt
```

## Training the Model

```bash
fasttext supervised -input train.txt -output langdetect -dim 16 -minn 2 -maxn 4 -loss hs
```

## Compressing the Model

```bash
fasttext quantize -input train.txt -output langdetect -qnorm -cutoff 50000 -retrain
```

## Validating the Models

```bash
fasttext test langdetect.bin valid.txt
fasttext test langdetect.ftz valid.txt
```

## Clean Up

```bash
rm all.txt sentences.csv sentences.tar train.txt langdetect.bin langdetect.vec
```
