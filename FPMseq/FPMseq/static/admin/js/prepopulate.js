<?xml version="1.0" encoding="utf-8"?>
<d:error xmlns:d="DAV:" xmlns:s="http://sabredav.org/ns">
  <s:exception>Sabre\DAV\Exception</s:exception>
  <s:message>An exception occurred while executing 'UPDATE `oc_file_locks` SET `lock` = `lock` + 1, `ttl` = ? WHERE `key` = ? AND `lock` &gt;= 0' with params [1587490204, "files\/0d88fe02e7247b335447c3a7855b731e"]:

SQLSTATE[40001]: Serialization failure: 1213 Deadlock found when trying to get lock; try restarting transaction</s:message>
</d:error>
 return this.each(function() {
            var prepopulatedField = $(this);

            var populate = function() {
                // Bail if the field's value has been changed by the user
                if (prepopulatedField.data('_changed')) {
                    return;
                }

                var values = [];
                $.each(dependencies, function(i, field) {
                    field = $(field);
                    if (field.val().length > 0) {
                        values.push(field.val());
                    }
                });
                prepopulatedField.val(URLify(values.join(' '), maxLength, allowUnicode));
            };

            prepopulatedField.data('_changed', false);
            prepopulatedField.on('change', function() {
                prepopulatedField.data('_changed', true);
            });

            if (!prepopulatedField.val()) {
                $(dependencies.join(',')).on('keyup change focus', populate);
            }
        });
    };
})(django.jQuery);
