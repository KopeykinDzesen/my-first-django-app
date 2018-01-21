$(document).ready(function () {

    var form = $('#form-buying_product');

    function basketUpdating(product_id, number) {
        var data = {};
        data.product_id = product_id;
        data.number = number;
        var csrf_token = $('#form-buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr('action');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                if (data.products_total_number || data.products_total_number == 0){
                    $('#basket_total_number').text('(' + data.products_total_number + ')');
                    $('.basket-items form').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items form').append('<div class="form-row  row-basket-item"' +
                            'id="basket_item_' + v.id + '">' +
                            '<div class="col-xl-10">' +
                            v.name + ' * ' + v.number + ' = ' + v.price_per_item * v.number + ' руб.' +
                            '</div><div class="col-xl-2"><button ' +
                            'class="btn btn-link btn-delete-product-in-basket"' +
                            'type="button" data-product_id="' + v.id + '">убрать</button>');
                    });
                    location.reload();
                };
            },
            error: function () {
                console.log('error')
            },
        });
    };
    
    form.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');

        basketUpdating(product_id, number);

    });

    function showingBasket() {
        $('.basket-items').toggleClass('hidden');
    };

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseover(function () {
        $('.basket-items').removeClass('hidden');
    });

    $('.basket-container').mouseout(function () {
       $('.basket-items').addClass('hidden');
    });
    
    function calculatingBasketAmount() {
        var total_order_amount = 0
        $('.total-product-in-basket-amount').each(function () {
            total_order_amount += parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };

    $(document).on('change', '.product-in-basket-number', function () {
        var current_number = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.produkt-in-basket-price').text());
        var total_price = current_number * current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_price.toFixed(2));

        calculatingBasketAmount();
    });

    calculatingBasketAmount();






    var form_basket_delete = $('#form_delete_product');

    function deletingProdactInBasket(product_id) {
        var data = {};
        data.product_id = product_id;

        var csrf_token = $('#form_delete_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form_basket_delete.attr('action');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log(data);

                $('#basket_total_number').text('(' + data.products_total_number + ')');
                    $('.basket-items form').html("");

                if (data.products_total_number){
                    $.each(data.products, function (k, v) {
                        $('.basket-items form').append('<div class="form-row  row-basket-item"' +
                            'id="basket_item_' + v.id + '">' +
                            '<div class="col-xl-10">' +
                            v.name + ' * ' + v.number + ' = ' + v.price_per_item * v.number + ' руб.' +
                            '</div><div class="col-xl-2"><button ' +
                            'class="btn btn-link btn-delete-product-in-basket"' +
                            'type="button" data-product_id="' + v.id + '">убрать</button>');
                    });
                    location.reload();
                };

            },
            error: function () {
                console.log('error')
            },
        });

    };

    $(document).on('click', '.btn-delete-product-in-basket', function () {
        var submit_btn = $(this);
        var product_id = submit_btn.data('product_id');
        console.log(product_id);

        deletingProdactInBasket(product_id);

    });

});