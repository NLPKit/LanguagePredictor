#  Tatoeba

## Dependencies

Run the following to install the `shuf` command on macOS:

```
brew install coreutils
```

## Preparing the Data

```
wget http://downloads.tatoeba.org/exports/sentences.tar.bz2
bunzip2 sentences.tar.bz2
tar xvf sentences.tar
awk -F"\t" '{print"__label__"$2" "$3}' < sentences.csv | shuf > all.txt
head -n 10000 all.txt > valid.txt
tail -n +10001 all.txt > train.txt
```

## Training the Model

```
fasttext supervised -input train.txt -output langdetect -dim 16 -minn 2 -maxn 4 -loss hs
```

## Compressing the Model

```
fasttext quantize -input train.txt -output langdetect -qnorm -cutoff 50000 -retrain
```

## Validating the Models

```
fasttext test langdetect.bin valid.txt
fasttext test langdetect.ftz valid.txt
```

## Clean Up

```
rm all.txt sentences.csv sentences.tar train.txt langdetect.bin langdetect.vec
```
