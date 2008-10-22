#!/bin/sh
dir=$RPM_BUILD_ROOT/usr/share/pear/Zend/Locale/Data
langfile=${1:-ZendFramework.lang}

> $langfile
find $dir -type f -name '*.xml' | while read file; do
	case "${file##*/}" in
	supplementalData.xml)
		# skip - no lang tag for this one
		continue
		;;
	esac

	language=$(sed -ne 's/<language type="\(.*\)"\/>/\1/p' $file | xargs)
	script=$(sed -ne 's/<script type="\(.*\)"\/>/\1/p' $file | xargs)
	territory=$(sed -ne 's/<territory type="\(.*\)"\/>/\1/p' $file | xargs)

	#<language type="sr"/>
	#<script type="Latn"/>
	#<territory type="BA"/>
	# sr_Latn_BA.xml -> sr_BA@Latn

	# TODO: <variant type="SAAHO"/>

	lang=$language${territory:+_$territory}${script:+@$script}
	file=${file#$RPM_BUILD_ROOT}
	echo "%lang($lang) ${file#$RPM_BUILD_ROOT}" >> $langfile
done
