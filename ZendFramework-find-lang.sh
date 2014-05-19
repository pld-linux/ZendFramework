#!/bin/sh

dir=$RPM_BUILD_ROOT/usr/share/pear/Zend/Locale/Data
langfile=${1:-ZendFramework.lang}

> $langfile
find $dir -type f -name '*.xml' | while read file; do
	case "${file##*/}" in
	characters.xml|\
	coverageLevels.xml|\
	dayPeriods.xml|\
	enderList.xml|\
	languageInfo.xml|\
	likelySubtags.xml|\
	metaZones.xml|\
	metazoneInfo.xml|\
	numberingSystems.xml|\
	ordinals.xml|\
	plurals.xml|\
	postalCodeData.xml|\
	root.xml|\
	supplementalData.xml|\
	supplementalMetadata.xml|\
	telephoneCodeData.xml|\
	-boo-\
	)
		# skip - no lang tag for this one
		continue
		;;
	esac

	echo >&2 "Inspect $file"
	language=$(sed -ne 's/<language type="\(.*\)"\/>/\1/p' $file | xargs)
	script=$(sed -ne 's/<script type="\(.*\)"\/>/\1/p' $file | xargs)
	territory=$(sed -ne 's/<territory type="\(.*\)"\/>/\1/p' $file | xargs)
	echo >&2 "${file%*/} language=$language; script=$script; territory=$territory"

	lang=$language${territory:+_$territory}${script:+@$script}
	file=${file#$RPM_BUILD_ROOT}
	if [ -n "$lang" ]; then
		echo "%lang($lang) ${file#$RPM_BUILD_ROOT}" >> $langfile
	fi
done
