SetDatePicker();

$(document).ready(function () {
    // Delete Item
    $('.item-row').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SaveItem(btn);
    });

    // Save form with ENTER
    $('.item-row').keyup('.transaction', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });







    // Servicer INFO
    // Delete Item
    $('.item-row-servicer').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row-servicer').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row-servicer').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SaveServicerItem(btn);
    });

    // Save form with ENTER
    $('.item-row-servicer').keyup('.servicer', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveServicerItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row-servicer').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row-servicer');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });






     // Plan INFO
    // Delete Item
    $('.item-row-plan').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row-plan').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row-plan').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SavePlanItem(btn);
    });

    // Save form with ENTER
    $('.item-row-plan').keyup('.plan', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SavePlanItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row-plan').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row-plan');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });




     // Product INFO
    // Delete Item
    $('.item-row-product').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row-product').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row-product').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SaveProductItem(btn);
    });

    // Save form with ENTER
    $('.item-row-product').keyup('.product', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveProductItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row-product').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row-product');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });







    // Store INFO
    // Delete Item
    $('.item-row-store').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row-store').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row-product').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SaveStoreItem(btn);
    });

    // Save form with ENTER
    $('.item-row-store').keyup('.store', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveStoreItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row-store').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row-store');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });





     // Customer INFO
    // Delete Item
    $('.item-row-customer').on('click', '.delete_item', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
                title: 'Warning!',
                content: 'Are you sure you want to delete?',
                type: 'red',
                buttons: {
                    yes: function () {
                        AjaxRemoveItem(param);
                    },
                    no: function () {
                    }
                }
            },
        );
    });

    // Edit Item by double click
    $('.item-row-customer').dblclick(function (event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row-customer').on('click', '.save_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        SaveCustomerItem(btn);
    });

    // Save form with ENTER
    $('.item-row-customer').keyup('.customer', function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveCustomerItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row-customer').on('click', '.cancel_form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row-customer');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });

    

});


// Functions
function AjaxGetEditRowDetail(param) {
    $.ajax({
        url: param['url'],
        type: 'GET',
        success: function (data) {
            param['item'].html(data.edit_row);
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}

function AjaxGetEditRowForm(param) {
    $.ajax({
        url: param['url'],
        type: 'GET',
        success: function (data) {
            param['item'].html(data.edit_row);
            SetDatePicker();
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}

function AjaxPutEditRowForm(param) {
    $.ajax({
        url: param['url'],
        type: 'PUT',
        data: param['query'],
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function (data) {
            notification[data.valid](data.message);

            if (data.valid === 'success') {
                param['item'].html(data.edit_row);
                SetDatePicker();
            }
        },
        error: function () {
            toastr.error('Error occurred');
        }
    });
}

function AjaxRemoveItem(param) {
    $.ajax({
        url: param['url'],
        type: 'DELETE',
        data: param['query'],
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function (data) {
            if (data.valid !== 'success')
                notification[data.valid](data.message);

            if (data.valid === 'success') {
                if (data.redirect_url) {
                    window.location.replace(data.redirect_url);
                } else {
                    notification[data.valid](data.message);
                    var item_row = param['btn'].closest('.item-row');
                    item_row.hide('slow', function () {
                        item_row.remove();
                    });
                }
            }
        },
        error: function () {
            toastr.error('Error occurred');
        }
    });
}

function SaveItem(btn) {
    var item = btn.closest('.item-row');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.transaction').serialize();
    AjaxPutEditRowForm(param);
}

function SaveServicerItem(btn) {
    var item = btn.closest('.item-row-servicer');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.servicer').serialize();
    AjaxPutEditRowForm(param);
}

function SavePlanItem(btn) {
    var item = btn.closest('.item-row-plan');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.plan').serialize();
    AjaxPutEditRowForm(param);
}

function SaveProductItem(btn) {
    var item = btn.closest('.item-row-product');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.product').serialize();
    AjaxPutEditRowForm(param);
}

function SaveStoreItem(btn) {
    var item = btn.closest('.item-row-store');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.store').serialize();
    AjaxPutEditRowForm(param);
}

function SaveCustomerItem(btn) {
    var item = btn.closest('.item-row-customer');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.customer').serialize();
    AjaxPutEditRowForm(param);
}


function SetDatePicker() {
    var datepickers = [].slice.call(d.querySelectorAll('.datepicker_input'));
    datepickers.map(function (el) {
        return new Datepicker(el, {format: 'yyyy-mm-dd'});
    });
}