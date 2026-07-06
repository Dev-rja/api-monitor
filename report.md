# API Reliability Monitor — SLA Report

> Last updated: **2026-07-06 22:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.76% | 2220.1 | 10206.7 | 1000ms | 267/1319 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.9 | 4595.4 | 1500ms | 4/1319 |
| ❌ | `nasa_apod` | 74.15% | 49.81% | 3368.7 | 11152.5 | 2000ms | 662/1319 |
| ❌ | `ipapi_check` | 76.5% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1319 |
| ⚠️ | `dog_ceo_random` | 95.53% | 96.82% | 530.8 | 10244.1 | 2500ms | 42/1319 |
| ⚠️ | `open_meteo_weather` | 98.56% | 96.89% | 734.5 | 14877.1 | 2000ms | 41/1319 |
| ⚠️ | `rest_countries` | 98.86% | 98.56% | 319.0 | 10221.5 | 2500ms | 19/1319 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.6 | 10229.6 | 2500ms | 4/1319 |
| ✅ | `catfact_random` | 99.77% | 99.32% | 256.3 | 10080.2 | 3000ms | 9/1319 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1319 |
| ✅ | `agify_name` | 99.92% | 99.7% | 383.7 | 16112.2 | 2000ms | 4/1319 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.2 | 3882.8 | 2000ms | 2/1319 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4367.1 | 63.89% |
| `nasa_apod` | 01:00 | 4222.8 | 60.53% |
| `nasa_apod` | 09:00 | 4216.7 | 54.39% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3790.7 | 53.62% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3588.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
